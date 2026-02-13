#!/usr/bin/env python3
"""
Silk CLI - Command Line Interface

Usage:
    silk run <file.silk>     Run a Silk program
    silk test <file.silk>    Run tests in a Silk file
    silk repl                Start interactive REPL
    silk --version           Show version
    silk --help              Show help
"""

import sys
import os
import subprocess

from . import Interpreter, __version__
from .lexer import Lexer
from .parser import Parser
from .errors import LexerError, ParseError, RuntimeError_
from .builtins.core import silk_repr
from .ast import (
    LetDeclaration, Assignment, CompoundAssignment,
    IfStatement, WhileLoop, ForLoop, DoWhileLoop, RepeatLoop,
    FunctionDef, ReturnStatement,
    StructDef, EnumDef, ImplBlock, InterfaceDef,
    ImportStmt, TestBlock, TryCatch, ThrowStatement,
)


SILK_BANNER = """
\033[96m╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ╔═╗╦╦  ╦╔═  ╦  ╔═╗╔╗╔╔═╗                                 ║
║   ╚═╗║║  ╠╩╗  ║  ╠═╣║║║║ ╦                                  ║
║   ╚═╝╩╩═╝╩ ╩  ╩═╝╩ ╩╝╚╝╚═╝  v{version}                        ║
║                                                              ║
║   Simple • Intuitive • Lightweight • Keen                    ║
║   Type 'help' for commands, 'exit' to quit                   ║
╚══════════════════════════════════════════════════════════════╝\033[0m
""".format(version=__version__)


HELP_TEXT = """
\033[93m━━━ Silk Language Quick Reference ━━━\033[0m

\033[96mVariables:\033[0m
  let name = "Silk"          // immutable
  let mut count = 0          // mutable
  count = count + 1

\033[96mFunctions:\033[0m
  fn greet(name: str) -> str {
      return "Hello, " + name
  }

\033[96mControl Flow:\033[0m
  if x > 0 { ... }
  elif x == 0 { ... }
  else { ... }

  while condition { ... }
  for i in range(10) { ... }
  do { ... } while condition
  repeat 5 { ... }

\033[96mStructs & Enums:\033[0m
  struct Patient { name: str, age: int }
  let p = Patient { name: "Ahmad", age: 8 }
  print(p.name)

  enum Status { Active, Inactive, Pending }
  let s = Status.Active

\033[96mPattern Matching:\033[0m
  match s {
      Active => print("active"),
      Inactive => print("inactive"),
      _ => print("other")
  }

\033[96mOption & Result:\033[0m
  let x = Some(42)
  match x {
      Some(v) => print(v),
      None => print("empty")
  }

  let r = Ok(100)
  match r {
      Ok(v) => print(v),
      Err(e) => print(e)
  }

\033[96mError Handling:\033[0m
  try { risky_operation() }
  catch e { print(e) }

\033[96mTesting:\033[0m
  test "my test" {
      assert 1 + 1 == 2
  }

\033[96mString Interpolation:\033[0m
  f"Hello {name}, age {age}"

\033[96mLambdas:\033[0m
  let double = |x| x * 2
  [1, 2, 3].map(|x| x * 2)

\033[96mModules:\033[0m
  import ./utils
  import silk/medical as med

\033[96mBuilt-in Functions:\033[0m
  print(x)              // output
  len(arr), range(n)    // collections
  sqrt(x), abs(x)       // math
  type(x), str(x)       // conversion
  push(arr, item)       // array ops
  sort(arr), reverse(arr)

\033[96mMedical Functions:\033[0m
  bmi(weight_kg, height_m)
  bsa(weight_kg, height_cm)
  dose_per_kg(mg_per_kg, weight_kg)
  ideal_body_weight(height_cm, is_male)
  mean(arr), median(arr), stdev(arr)

\033[96mREPL Commands:\033[0m
  help     - Show this help
  clear    - Clear screen
  exit     - Exit REPL
"""

# Statement types that should NOT auto-print in REPL
_REPL_STATEMENT_TYPES = (
    LetDeclaration, Assignment, CompoundAssignment,
    IfStatement, WhileLoop, ForLoop, DoWhileLoop, RepeatLoop,
    FunctionDef, ReturnStatement,
    StructDef, EnumDef, ImplBlock, InterfaceDef,
    ImportStmt, TestBlock, TryCatch, ThrowStatement,
)


def clear_screen():
    """Clear the terminal screen safely."""
    if os.name == 'nt':
        subprocess.run(['cmd', '/c', 'cls'], check=False)
    else:
        subprocess.run(['clear'], check=False)


def repl():
    """Start the interactive REPL."""
    print(SILK_BANNER)
    interpreter = Interpreter()
    buffer = []
    brace_depth = 0

    while True:
        try:
            prompt = "\033[92msilk>\033[0m " if not buffer else "\033[90m  ...\033[0m "
            line = input(prompt)

            # REPL commands
            stripped = line.strip()
            if not buffer:
                if stripped in ('exit', 'quit'):
                    print("\033[96mGoodbye!\033[0m")
                    break
                if stripped == 'help':
                    print(HELP_TEXT)
                    continue
                if stripped == 'clear':
                    clear_screen()
                    print(SILK_BANNER)
                    continue
                if stripped == '':
                    continue

            buffer.append(line)
            brace_depth += line.count('{') - line.count('}')

            if brace_depth <= 0:
                source = '\n'.join(buffer)
                buffer = []
                brace_depth = 0

                # For single expressions, print the result
                try:
                    lexer = Lexer(source)
                    tokens = lexer.tokenize()
                    parser = Parser(tokens)
                    ast = parser.parse()

                    if (len(ast.statements) == 1 and
                        not isinstance(ast.statements[0], _REPL_STATEMENT_TYPES)):
                        result = interpreter.evaluate(
                            ast.statements[0], interpreter.global_env
                        )
                        if result is not None:
                            print(f"\033[93m-> {silk_repr(result)}\033[0m")
                    else:
                        interpreter.execute(ast, interpreter.global_env)

                except (LexerError, ParseError, RuntimeError_) as e:
                    print(f"\033[91mError: {e}\033[0m")

        except KeyboardInterrupt:
            print("\n\033[96m(Use 'exit' to quit)\033[0m")
            buffer = []
            brace_depth = 0
        except EOFError:
            print("\n\033[96mGoodbye!\033[0m")
            break


def run_file(filepath: str) -> bool:
    """Run a Silk source file."""
    from pathlib import Path

    file_path = Path(filepath).resolve()
    if not file_path.exists():
        print(f"Error: File not found: {filepath}")
        return False

    source = file_path.read_text(encoding='utf-8')
    interpreter = Interpreter()
    return interpreter.run(source, file_path=file_path)


def test_file(filepath: str) -> bool:
    """Run tests in a Silk source file."""
    from pathlib import Path

    file_path = Path(filepath).resolve()
    if not file_path.exists():
        print(f"Error: File not found: {filepath}")
        return False

    source = file_path.read_text(encoding='utf-8')
    interpreter = Interpreter()

    print(f"\033[96mRunning tests in {file_path.name}...\033[0m\n")

    try:
        results = interpreter.run_tests(source, file_path=file_path)
    except Exception as e:
        print(f"\n\033[91mError: {e}\033[0m")
        return False

    # Print captured output
    for line in interpreter.output_lines:
        if line.startswith("  PASS:"):
            print(f"\033[92m  {line[8:]}\033[0m")
        elif line.startswith("  FAIL:"):
            print(f"\033[91m  {line[8:]}\033[0m")
        elif line.startswith("    "):
            print(f"\033[91m{line}\033[0m")
        else:
            print(line)

    if results['failed'] == 0 and results['total'] > 0:
        print(f"\n\033[92mAll {results['total']} tests passed!\033[0m")
    elif results['total'] == 0:
        print("\033[93mNo tests found.\033[0m")

    return results['failed'] == 0


def show_help():
    """Show CLI help."""
    print(f"""
Silk Programming Language v{__version__}
Simple . Intuitive . Lightweight . Keen

Usage:
    silk run <file.silk>     Run a Silk program
    silk test <file.silk>    Run tests in a Silk file
    silk repl                Start interactive REPL
    silk                     Start interactive REPL (default)
    silk --version, -v       Show version
    silk --help, -h          Show this help

Examples:
    silk run hello.silk      Run hello.silk
    silk test tests.silk     Run tests in tests.silk
    silk repl                Start REPL
    silk                     Start REPL
""")


def main():
    """Main entry point."""
    args = sys.argv[1:]

    if not args:
        repl()
        return

    cmd = args[0]

    if cmd in ('--version', '-v'):
        print(f"Silk {__version__}")

    elif cmd in ('--help', '-h'):
        show_help()

    elif cmd == 'repl':
        repl()

    elif cmd == 'run':
        if len(args) < 2:
            print("Error: Missing file argument. Usage: silk run <file.silk>")
            sys.exit(1)
        success = run_file(args[1])
        if not success:
            sys.exit(1)

    elif cmd == 'test':
        if len(args) < 2:
            print("Error: Missing file argument. Usage: silk test <file.silk>")
            sys.exit(1)
        success = test_file(args[1])
        if not success:
            sys.exit(1)

    else:
        # Assume it's a file path
        if os.path.exists(cmd):
            success = run_file(cmd)
            if not success:
                sys.exit(1)
        else:
            print(f"Error: Unknown command: {cmd}")
            print("Run 'silk --help' for usage.")
            sys.exit(1)


if __name__ == '__main__':
    main()
