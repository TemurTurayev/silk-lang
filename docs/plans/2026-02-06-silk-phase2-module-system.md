# Silk Phase 2: Module/Import System

> **Design Principle:** Always-namespaced imports. No scope pollution. Medical safety through explicitness.

**Goal:** Add a module/import system so Silk programs can be split across files, reuse code, and access stdlib modules — all with mandatory namespace prefixes for clarity.

---

## Syntax

```silk
import silk/math                        // stdlib → namespace "math"
import silk/medical/pediatrics as ped   // stdlib → namespace "ped"
import ./utils                          // relative → namespace "utils"
import ./lib/geometry as geo            // relative → namespace "geo"
```

**Rules:**
- Every import is namespaced (no bare `from X import Y`)
- `as` alias is optional; default = last path segment
- `.silk` extension is implicit
- No quoted strings — bare path style

---

## Path Resolution

Tried in order:

1. **`silk/` prefix** → Standard library or native module
   - File: `<stdlib_dir>/<path>.silk`
   - Or virtual/native module (Python bindings)
2. **`./` prefix** → Relative to importing file's directory
3. **No prefix** → Same as `./` (relative to current file)

Default namespace = last path segment:
- `import silk/medical/pediatrics` → `pediatrics`
- `import ./lib/geometry` → `geometry`

---

## Runtime

### Execution Flow

```
1. Parser produces ImportStmt(path, alias)
2. Interpreter.execute(ImportStmt):
   a. Resolve path → absolute file path (or native module ID)
   b. Check _module_cache → if cached, skip to (f)
   c. Check _loading_set → if present, raise "Circular import" error
   d. Add to _loading_set
   e. Read file → Lexer → Parser → execute in fresh Environment
   f. Remove from _loading_set, store in _module_cache
   g. Bind: env.define(alias, module_env, mutable=False)
```

### Namespace Access

`math.sqrt(16)` parses as `MemberAccess(Identifier("math"), "sqrt")`.

`_eval_member` extended: if obj is an `Environment`, look up member in that environment.

### Module Cache

- `_module_cache: dict[str, Environment]` keyed by absolute path
- `_loading_set: set[str]` for circular import detection
- First import executes; subsequent imports return cached env

### Native Modules

Virtual modules backed by Python for performance-critical code:

```python
def _load_native_module(self, name: str) -> Environment:
    env = Environment()
    if name == "silk/math":
        env.define("sqrt", ('builtin', builtin_sqrt), mutable=False)
        env.define("pi", 3.14159265358979, mutable=False)
    return env
```

Existing builtins remain global (no breaking change). Native modules provide namespaced access to the same functions.

---

## Implementation Tasks

| Task | Description | Files |
|------|-------------|-------|
| 2.1 | Add `ImportStmt` AST node | `ast.py` |
| 2.2 | Parse `import path` and `import path as alias` | `parser.py`, tests |
| 2.3 | Path resolver function | new `resolver.py`, tests |
| 2.4 | Module cache + circular import detection | `interpreter.py`, tests |
| 2.5 | Execute file-based imports | `interpreter.py`, tests |
| 2.6 | Namespace access via `_eval_member` on Environment | `interpreter.py`, tests |
| 2.7 | Native module support (`silk/math`) | `interpreter.py`, tests |
| 2.8 | Golden test: multi-file program | `tests/golden/` |
| 2.9 | CLI update: resolve imports relative to entry file | `cli/silk_cli.py` |

### Test Strategy

- `tests/test_types/test_modules.py` for unit/integration tests
- `tests/fixtures/modules/` directory with small `.silk` files
- Golden test with multi-file imports

---

## Stdlib Structure (Future)

```
stdlib/
  ├── math.silk         (wraps native math)
  ├── collections.silk  (advanced data structures)
  └── medical/
      ├── dosing.silk
      ├── labs.silk
      └── units.silk
```

Native modules come first; `.silk` stdlib files come later.
