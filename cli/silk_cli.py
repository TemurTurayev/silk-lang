#!/usr/bin/env python3
"""
Silk CLI - Command Line Interface

Usage:
    silk run <file.silk>     Run a Silk program
    silk repl                Start interactive REPL
    silk --version           Show version
    silk --help              Show help
"""

import sys
import os
import subprocess

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from silk import Interpreter, __version__
from silk.lexer import Lexer
from silk.parser import Parser
from silk.errors import LexerError, ParseError, RuntimeError_
from silk.builtins.core import silk_repr
from silk.ast import (
    LetDeclaration, Assignment, CompoundAssignment,
    IfStatement, WhileLoop, ForLoop, FunctionDef, ReturnStatement
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
  for item in array { ... }

\033[96mData Types:\033[0m
  42, 3.14              // numbers
  "hello"               // string
  true, false           // booleans
  [1, 2, 3]             // array
  null                  // null

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
                    print("\033[96m👋 Goodbye!\033[0m")
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
                        not isinstance(ast.statements[0], (
                            LetDeclaration, Assignment, CompoundAssignment,
                            IfStatement, WhileLoop, ForLoop,
                            FunctionDef, ReturnStatement
                        ))):
                        result = interpreter.evaluate(
                            ast.statements[0], interpreter.global_env
                        )
                        if result is not None:
                            print(f"\033[93m→ {silk_repr(result)}\033[0m")
                    else:
                        interpreter.execute(ast, interpreter.global_env)

                except (LexerError, ParseError, RuntimeError_) as e:
                    print(f"\033[91m❌ {e}\033[0m")

        except KeyboardInterrupt:
            print("\n\033[96m(Use 'exit' to quit)\033[0m")
            buffer = []
            brace_depth = 0
        except EOFError:
            print("\n\033[96m👋 Goodbye!\033[0m")
            break


def run_file(filepath: str) -> bool:
    """Run a Silk source file."""
    from pathlib import Path

    file_path = Path(filepath).resolve()
    if not file_path.exists():
        print(f"❌ File not found: {filepath}")
        return False

    source = file_path.read_text(encoding='utf-8')
    interpreter = Interpreter()
    return interpreter.run(source, file_path=file_path)


def show_help():
    """Show CLI help."""
    print(f"""
Silk Programming Language v{__version__}
Simple • Intuitive • Lightweight • Keen

Usage:
    silk run <file.silk>     Run a Silk program
    silk repl                Start interactive REPL
    silk                     Start interactive REPL (default)
    silk --version, -v       Show version
    silk --help, -h          Show this help

Examples:
    silk run hello.silk      Run hello.silk
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
            print("❌ Missing file argument. Usage: silk run <file.silk>")
            sys.exit(1)
        success = run_file(args[1])
        if not success:
            sys.exit(1)

    else:
        # Assume it's a file path
        if os.path.exists(cmd):
            success = run_file(cmd)
            if not success:
                sys.exit(1)
        else:
            print(f"❌ Unknown command: {cmd}")
            print("Run 'silk --help' for usage.")
            sys.exit(1)


if __name__ == '__main__':
    main()
