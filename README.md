# Silk Programming Language

**Simple . Intuitive . Lightweight . Keen**

Silk is a programming language designed for medical computing with clean syntax inspired by Python (simplicity), Go (clarity), and Rust (safety). It features immutability by default, exhaustive pattern matching, and built-in medical functions.

> **"A language where a programmer writes code that a doctor can READ and VERIFY"**

## Quick Start

```bash
# Install
pip install silk-lang

# Or install from source
git clone https://github.com/TemurTurayev/silk-lang.git
cd silk-lang
pip install -e .

# Run a program
silk run hello.silk

# Run tests
silk test tests.silk

# Interactive REPL
silk repl
```

## Language Features

### Variables

```silk
let name = "Silk"           // immutable (default)
let mut count = 0           // mutable (explicit)
count = count + 1           // OK
// name = "other"           // ERROR: immutable!

let age: int = 25           // with type hint
```

### Data Types

```silk
42, 3.14                    // int, float
"hello", 'world'            // strings
true, false                 // booleans
[1, 2, 3]                   // arrays
{"name": "Silk", "v": 2}   // maps (dictionaries)
null                        // null
Some(42), None              // Option<T>
Ok(100), Err("fail")       // Result<T, E>
```

### Functions

```silk
fn add(a: int, b: int) -> int {
    return a + b
}

fn greet(name: str) {
    print(f"Hello, {name}!")
}

// Lambdas
let double = |x| x * 2
[1, 2, 3].map(|x| x * 2)    // [2, 4, 6]
```

### Control Flow

```silk
// Conditionals
if score >= 90 {
    print("Excellent!")
} elif score >= 70 {
    print("Good")
} else {
    print("Keep trying")
}

// Loops
for i in range(10) { print(i) }
for item in [1, 2, 3] { print(item) }

while x < 10 { x += 1 }

do { x += 1 } while x < 10

repeat 5 { print("Hello") }
```

### Structs

```silk
struct Patient {
    id: str,
    name: str,
    age: int,
    weight: float,
    height: float
}

let patient = Patient {
    id: "P001",
    name: "Ahmad",
    age: 8,
    weight: 25.0,
    height: 1.20
}

print(patient.name)       // "Ahmad"
print(patient.weight)     // 25.0
```

### Enums

```silk
enum BMICategory {
    Underweight,
    Normal,
    Overweight,
    Obese
}

let category = BMICategory.Normal
```

### Pattern Matching

Matches must be **exhaustive** — all variants must be covered. This is critical for medical safety: silent missed cases are not allowed.

```silk
// Exhaustive match on enum (all variants covered)
match category {
    Underweight => print("Consider nutritional support"),
    Normal => print("Healthy weight"),
    Overweight => print("Recommend lifestyle changes"),
    Obese => print("Medical intervention needed")
}
// Missing a variant = COMPILE ERROR!

// Wildcard for catch-all
match value {
    1 => print("one"),
    2 => print("two"),
    _ => print("other")
}

// Guards
match bmi_value {
    _ if bmi_value < 18.5 => print("Underweight"),
    _ if bmi_value < 25.0 => print("Normal"),
    _ => print("Above normal")
}
```

### Option and Result

```silk
// Option<T>: Some(value) or None
let x = Some(42)
match x {
    Some(v) => print(v),
    None => print("empty")
}

// Result<T, E>: Ok(value) or Err(error)
fn safe_divide(a: float, b: float) -> Result {
    if b == 0.0 {
        return Err("Division by zero")
    }
    return Ok(a / b)
}

match safe_divide(10.0, 3.0) {
    Ok(result) => print(result),
    Err(e) => print(f"Error: {e}")
}
```

### Impl Blocks

```silk
impl Patient {
    fn bmi(self) -> float {
        return bmi(self.weight, self.height)
    }

    fn is_adult(self) -> bool {
        return self.age >= 18
    }
}

print(patient.bmi())        // 17.36
print(patient.is_adult())   // false
```

### Interfaces

```silk
interface Calculable {
    fn calculate(self) -> float
}

impl Calculable for Patient {
    fn calculate(self) -> float {
        return self.weight
    }
}
```

### Error Handling

```silk
// try/catch
try {
    let result = risky_operation()
} catch e {
    print(f"Error: {e}")
}

// throw
if weight <= 0 {
    throw "Weight must be positive"
}
```

### Modules

```silk
import ./utils               // relative import
import silk/medical as med   // stdlib with alias

med.bmi(70.0, 1.75)
```

### Testing

```silk
test "BMI calculation" {
    assert bmi(70.0, 1.75) > 22
    assert bmi(70.0, 1.75) < 23
}

test "safe division" {
    let result = safe_divide(10.0, 0.0)
    match result {
        Err(e) => assert e == "Division by zero",
        _ => assert false
    }
}
```

Run tests with: `silk test myfile.silk`

### String Interpolation

```silk
let name = "Ahmad"
let age = 8
print(f"Patient {name} is {age} years old")
```

## Built-in Functions

| Category | Functions |
|----------|-----------|
| **I/O** | `print()`, `input()` |
| **Types** | `type()`, `typeof()`, `str()`, `int()`, `float()`, `bool()` |
| **Collections** | `len()`, `range()`, `push()`, `pop()`, `shift()`, `unshift()`, `sort()`, `reverse()` |
| **Array Ops** | `map()`, `filter()`, `find()`, `reduce()`, `forEach()`, `zip()`, `flatten()`, `contains()`, `indexOf()` |
| **String Ops** | `join()`, `split()`, `trim()`, `replace()`, `toUpperCase()`, `toLowerCase()` |
| **Math** | `abs()`, `round()`, `min()`, `max()`, `sum()`, `sqrt()`, `pow()`, `ceil()`, `floor()`, `pi()` |
| **Trig** | `sin()`, `cos()`, `tan()`, `log()`, `log10()` |
| **Statistics** | `mean()`, `median()`, `stdev()` |
| **Medical** | `bmi()`, `bsa()`, `dose_per_kg()`, `ideal_body_weight()`, `celsius_to_fahrenheit()`, `fahrenheit_to_celsius()` |

## Medical Functions

All medical functions compute only — they do not diagnose or recommend treatment.

> **Disclaimer:** Results require clinical interpretation. Not medical advice.

```silk
// Body Mass Index (kg/m^2)
bmi(70.0, 1.75)                      // 22.86

// Body Surface Area - Du Bois formula (m^2)
bsa(70.0, 175.0)                     // 1.85

// Weight-based dosing (mg)
dose_per_kg(15.0, 25.0)              // 375.0

// Ideal Body Weight - Devine formula (kg)
ideal_body_weight(175.0, true)       // 70.6

// Temperature conversion
celsius_to_fahrenheit(37.0)          // 98.6
fahrenheit_to_celsius(98.6)          // 37.0

// Statistics
mean([36.6, 36.8, 37.1])            // 36.83
median([1, 3, 5, 7, 9])             // 5
stdev([2, 4, 6, 8])                  // 2.58
```

## VS Code Extension

The `vscode-silk/` directory contains a VS Code extension with syntax highlighting:

```bash
cd vscode-silk
# Install in VS Code
code --install-extension .
```

Features:
- Syntax highlighting for all keywords, operators, and built-in functions
- f-string interpolation highlighting
- Auto-closing pairs for brackets, quotes, and braces
- Comment toggling (`//` and `/* */`)

## Examples

See the `examples/` directory:

- `examples/patient_assessment.silk` — Full medical example with struct, enum, match, and Result
- `examples/test_dosing.silk` — Testing example with assertions

## Design Principles

- **Immutability by default** — prevents accidental mutations in medical code
- **Exhaustive pattern matching** — no silent missed cases
- **Error-as-value** — Result/Option types for explicit error handling
- **Medical safety** — computes but never diagnoses or recommends
- **Readability over writability** — doctors can read and verify the logic

## Requirements

- Python 3.11+
- Zero external dependencies

## License

MIT

---

*Created by Temur Turayev | TashPMI | 2026*
