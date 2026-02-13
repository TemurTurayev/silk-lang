"""
Silk LSP Completion Data

Function signatures, documentation, and keyword info for IDE features.
"""

from lsprotocol.types import (
    CompletionItem,
    CompletionItemKind,
    InsertTextFormat,
    MarkupContent,
    MarkupKind,
)


# ─── Keywords ──────────────────────────────────────────────
KEYWORD_ITEMS: list[CompletionItem] = [
    CompletionItem(
        label="let",
        kind=CompletionItemKind.Keyword,
        insert_text="let ${1:name} = ${2:value}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Variable declaration (immutable)",
        documentation=MarkupContent(
            kind=MarkupKind.Markdown,
            value="```silk\nlet name = value    // immutable\nlet mut x = 0       // mutable\nlet age: int = 25   // with type hint\n```",
        ),
    ),
    CompletionItem(
        label="let mut",
        kind=CompletionItemKind.Keyword,
        insert_text="let mut ${1:name} = ${2:value}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Mutable variable declaration",
    ),
    CompletionItem(
        label="fn",
        kind=CompletionItemKind.Keyword,
        insert_text="fn ${1:name}(${2:params}) {\n\t${3}\n}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Function definition",
        documentation=MarkupContent(
            kind=MarkupKind.Markdown,
            value="```silk\nfn add(a: int, b: int) -> int {\n    return a + b\n}\n```",
        ),
    ),
    CompletionItem(
        label="struct",
        kind=CompletionItemKind.Keyword,
        insert_text="struct ${1:Name} {\n\t${2:field}: ${3:type}\n}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Struct definition",
        documentation=MarkupContent(
            kind=MarkupKind.Markdown,
            value="```silk\nstruct Patient {\n    id: str,\n    name: str,\n    age: int\n}\n```",
        ),
    ),
    CompletionItem(
        label="enum",
        kind=CompletionItemKind.Keyword,
        insert_text="enum ${1:Name} {\n\t${2:Variant1},\n\t${3:Variant2}\n}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Enum definition",
    ),
    CompletionItem(
        label="match",
        kind=CompletionItemKind.Keyword,
        insert_text="match ${1:value} {\n\t${2:pattern} => ${3:expr},\n\t_ => ${4:default}\n}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Pattern matching (exhaustive)",
        documentation=MarkupContent(
            kind=MarkupKind.Markdown,
            value="Matches must be **exhaustive** \u2014 all variants must be covered.\n\n```silk\nmatch category {\n    Underweight => print(\"low\"),\n    Normal => print(\"ok\"),\n    _ => print(\"high\")\n}\n```",
        ),
    ),
    CompletionItem(
        label="impl",
        kind=CompletionItemKind.Keyword,
        insert_text="impl ${1:Type} {\n\tfn ${2:method}(self) {\n\t\t${3}\n\t}\n}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Implementation block",
    ),
    CompletionItem(
        label="interface",
        kind=CompletionItemKind.Keyword,
        insert_text="interface ${1:Name} {\n\tfn ${2:method}(self) -> ${3:type}\n}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Interface definition",
    ),
    CompletionItem(
        label="if",
        kind=CompletionItemKind.Keyword,
        insert_text="if ${1:condition} {\n\t${2}\n}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Conditional",
    ),
    CompletionItem(
        label="elif",
        kind=CompletionItemKind.Keyword,
        detail="Else-if branch",
    ),
    CompletionItem(
        label="else",
        kind=CompletionItemKind.Keyword,
        detail="Else branch",
    ),
    CompletionItem(
        label="for",
        kind=CompletionItemKind.Keyword,
        insert_text="for ${1:item} in ${2:collection} {\n\t${3}\n}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="For loop",
    ),
    CompletionItem(
        label="while",
        kind=CompletionItemKind.Keyword,
        insert_text="while ${1:condition} {\n\t${2}\n}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="While loop",
    ),
    CompletionItem(
        label="do",
        kind=CompletionItemKind.Keyword,
        insert_text="do {\n\t${1}\n} while ${2:condition}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Do-while loop",
    ),
    CompletionItem(
        label="repeat",
        kind=CompletionItemKind.Keyword,
        insert_text="repeat ${1:n} {\n\t${2}\n}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Repeat N times",
    ),
    CompletionItem(
        label="test",
        kind=CompletionItemKind.Keyword,
        insert_text='test "${1:description}" {\n\tassert ${2:condition}\n}',
        insert_text_format=InsertTextFormat.Snippet,
        detail="Test block",
        documentation=MarkupContent(
            kind=MarkupKind.Markdown,
            value='```silk\ntest "BMI calculation" {\n    assert bmi(70.0, 1.75) > 22\n    assert bmi(70.0, 1.75) < 23\n}\n```',
        ),
    ),
    CompletionItem(
        label="try",
        kind=CompletionItemKind.Keyword,
        insert_text="try {\n\t${1}\n} catch ${2:e} {\n\t${3}\n}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Try-catch error handling",
    ),
    CompletionItem(
        label="import",
        kind=CompletionItemKind.Keyword,
        insert_text="import ${1:module}",
        insert_text_format=InsertTextFormat.Snippet,
        detail="Module import",
    ),
    CompletionItem(label="return", kind=CompletionItemKind.Keyword, detail="Return from function"),
    CompletionItem(label="break", kind=CompletionItemKind.Keyword, detail="Break out of loop"),
    CompletionItem(label="continue", kind=CompletionItemKind.Keyword, detail="Continue to next iteration"),
    CompletionItem(label="throw", kind=CompletionItemKind.Keyword, detail="Throw an error"),
    CompletionItem(label="assert", kind=CompletionItemKind.Keyword, detail="Assert condition in test"),
    CompletionItem(label="true", kind=CompletionItemKind.Constant, detail="Boolean true"),
    CompletionItem(label="false", kind=CompletionItemKind.Constant, detail="Boolean false"),
    CompletionItem(label="null", kind=CompletionItemKind.Constant, detail="Null value"),
    CompletionItem(label="self", kind=CompletionItemKind.Keyword, detail="Self reference in impl"),
]


# ─── Function signature helper ─────────────────────────────
def _fn(
    name: str,
    signature: str,
    doc: str,
    kind: CompletionItemKind = CompletionItemKind.Function,
    snippet: str | None = None,
) -> CompletionItem:
    return CompletionItem(
        label=name,
        kind=kind,
        insert_text=snippet or f"{name}(${{1}})",
        insert_text_format=InsertTextFormat.Snippet,
        detail=signature,
        documentation=MarkupContent(
            kind=MarkupKind.Markdown,
            value=doc,
        ),
    )


# ─── Core Built-in Functions ──────────────────────────────
CORE_FUNCTION_ITEMS: list[CompletionItem] = [
    _fn("print", "print(...values)", "Print values to stdout.\n\n```silk\nprint(\"Hello\")\nprint(patient.name, patient.age)\n```"),
    _fn("input", "input(prompt?) -> str", "Read input from stdin.\n\n```silk\nlet name = input(\"Enter name: \")\n```"),
    _fn("type", "type(value) -> str", "Get the type name of a value.\n\nReturns: `\"int\"`, `\"float\"`, `\"str\"`, `\"bool\"`, `\"array\"`, `\"map\"`, `\"null\"`, `\"function\"`, `\"decimal\"`, `\"unit\"`"),
    _fn("str", "str(value) -> str", "Convert value to string."),
    _fn("int", "int(value) -> int", "Convert value to integer."),
    _fn("float", "float(value) -> float", "Convert value to float."),
    _fn("bool", "bool(value) -> bool", "Convert value to boolean."),
    _fn("len", "len(collection) -> int", "Get length of array, string, or map."),
    _fn("range", "range(stop) / range(start, stop, step?)", "Generate a range of integers.\n\n```silk\nrange(5)        // [0, 1, 2, 3, 4]\nrange(1, 5)     // [1, 2, 3, 4]\nrange(0, 10, 2) // [0, 2, 4, 6, 8]\n```", snippet="range(${1:stop})"),
    _fn("push", "push(array, item) -> array", "Append item to array."),
    _fn("pop", "pop(array) -> value", "Remove and return last item."),
    _fn("slice", "slice(array, start?, end?) -> array", "Get a slice of array or string."),
    _fn("reverse", "reverse(array) -> array", "Reverse array or string."),
    _fn("sort", "sort(array) -> array", "Sort array (returns new sorted array)."),
    _fn("join", "join(array, separator?) -> str", "Join array elements into string.\n\n```silk\njoin([\"a\", \"b\", \"c\"], \", \") // \"a, b, c\"\n```"),
    _fn("split", "split(str, separator?) -> array", "Split string into array."),
    _fn("contains", "contains(collection, item) -> bool", "Check if collection contains item."),
    _fn("map", "map(array, fn) -> array", "Map a function over array.\n\n```silk\nmap([1, 2, 3], |x| x * 2) // [2, 4, 6]\n```"),
    _fn("filter", "filter(array, fn) -> array", "Filter array with predicate.\n\n```silk\nfilter([1, 2, 3, 4], |x| x > 2) // [3, 4]\n```"),
    _fn("reduce", "reduce(array, fn, initial) -> value", "Reduce array to single value.\n\n```silk\nreduce([1, 2, 3], |acc, x| acc + x, 0) // 6\n```"),
    _fn("forEach", "forEach(array, fn)", "Iterate over array (no return)."),
    _fn("zip", "zip(a, b) -> array", "Zip two arrays into pairs."),
    _fn("decimal", "decimal(value) -> Decimal", "Create precise decimal value.\n\nAvoids float rounding for medical dosing.\n\n```silk\nlet a = decimal(\"0.1\")\nlet b = decimal(\"0.2\")\nprint(a + b) // exactly 0.3\n```"),
    _fn("unit", "unit(value, unit_name) -> Unit", "Create a value with physical unit.\n\nPrevents dangerous unit mismatches.\n\n```silk\nlet dose = unit(500, \"mg\")\nlet vol = unit(100, \"mL\")\n// dose + vol -> ERROR: mg vs mL\n```", snippet='unit(${1:value}, "${2:unit}")'),
]

# ─── Option/Result constructors ────────────────────────────
CONSTRUCTOR_ITEMS: list[CompletionItem] = [
    _fn("Some", "Some(value) -> Option", "Create a Some(value) Option.\n\n```silk\nlet x = Some(42)\nmatch x {\n    Some(v) => print(v),\n    None => print(\"empty\")\n}\n```"),
    _fn("Ok", "Ok(value) -> Result", "Create an Ok(value) Result.\n\n```silk\nreturn Ok(computed_dose)\n```"),
    _fn("Err", "Err(error) -> Result", "Create an Err(error) Result.\n\n```silk\nreturn Err(\"Division by zero\")\n```"),
    CompletionItem(
        label="None",
        kind=CompletionItemKind.Constant,
        detail="Empty Option value",
        documentation=MarkupContent(
            kind=MarkupKind.Markdown,
            value="Represents an absent value in `Option<T>`.",
        ),
    ),
]


# ─── Math Functions ────────────────────────────────────────
MATH_FUNCTION_ITEMS: list[CompletionItem] = [
    _fn("abs", "abs(x) -> number", "Absolute value."),
    _fn("round", "round(x, decimals?) -> number", "Round to n decimal places."),
    _fn("min", "min(a, b) / min(array) -> number", "Minimum value."),
    _fn("max", "max(a, b) / max(array) -> number", "Maximum value."),
    _fn("sum", "sum(array) -> number", "Sum of values."),
    _fn("sqrt", "sqrt(x) -> float", "Square root."),
    _fn("pow", "pow(base, exp) -> float", "Power function."),
    _fn("log", "log(x, base?) -> float", "Natural log (or with base)."),
    _fn("log10", "log10(x) -> float", "Base-10 logarithm."),
    _fn("sin", "sin(x) -> float", "Sine (radians)."),
    _fn("cos", "cos(x) -> float", "Cosine (radians)."),
    _fn("tan", "tan(x) -> float", "Tangent (radians)."),
    _fn("pi", "pi() -> float", "Pi constant (3.14159...)."),
    _fn("ceil", "ceil(x) -> int", "Ceiling (round up)."),
    _fn("floor", "floor(x) -> int", "Floor (round down)."),
]


# ─── Medical Functions ─────────────────────────────────────
_MED_DISCLAIMER = "\n\n> \u26a0\ufe0f Results require clinical interpretation. Not medical advice."

MEDICAL_FUNCTION_ITEMS: list[CompletionItem] = [
    # Anthropometric
    _fn("bmi", "bmi(weight_kg, height_m) -> float",
         f"**Body Mass Index** (kg/m\u00b2)\n\nFormula: `weight / height\u00b2`\n\n```silk\nbmi(70.0, 1.75)  // 22.86\n```{_MED_DISCLAIMER}",
         snippet="bmi(${1:weight_kg}, ${2:height_m})"),
    _fn("bsa", "bsa(weight_kg, height_cm) -> float",
         f"**Body Surface Area** \u2014 Du Bois formula (m\u00b2)\n\nFormula: `0.007184 \u00d7 weight\u2070\u00b7\u2074\u00b2\u2075 \u00d7 height\u2070\u00b7\u2077\u00b2\u2075`\n\n```silk\nbsa(70.0, 175.0)  // 1.85\n```{_MED_DISCLAIMER}",
         snippet="bsa(${1:weight_kg}, ${2:height_cm})"),
    _fn("ideal_body_weight", "ideal_body_weight(height_cm, is_male) -> float",
         f"**Ideal Body Weight** \u2014 Devine formula (kg)\n\nMale: `50 + 0.91 \u00d7 (height - 152.4)`\nFemale: `45.5 + 0.91 \u00d7 (height - 152.4)`{_MED_DISCLAIMER}",
         snippet="ideal_body_weight(${1:height_cm}, ${2:is_male})"),
    _fn("bmi_category", "bmi_category(bmi_value) -> str",
         f"Return BMI category string.\n\nReturns: `\"underweight\"`, `\"normal\"`, `\"overweight\"`, `\"obese\"`{_MED_DISCLAIMER}"),

    # Renal
    _fn("creatinine_clearance", "creatinine_clearance(age, weight_kg, creatinine, is_male) -> float",
         f"**Creatinine Clearance** \u2014 Cockcroft-Gault (mL/min)\n\nFormula: `((140 - age) \u00d7 weight) / (72 \u00d7 creatinine)` [\u00d7 0.85 if female]{_MED_DISCLAIMER}",
         snippet="creatinine_clearance(${1:age}, ${2:weight_kg}, ${3:creatinine}, ${4:is_male})"),
    _fn("egfr", "egfr(creatinine, age, is_male) -> float",
         f"**Estimated GFR** \u2014 CKD-EPI 2021 (mL/min/1.73m\u00b2)\n\nRace-free equation.{_MED_DISCLAIMER}",
         snippet="egfr(${1:creatinine}, ${2:age}, ${3:is_male})"),

    # Pediatric
    _fn("pediatric_dose", "pediatric_dose(adult_dose_mg, child_weight_kg) -> float",
         f"**Pediatric dose** \u2014 Clark's rule (mg)\n\nFormula: `(child_weight / 70) \u00d7 adult_dose`{_MED_DISCLAIMER}",
         snippet="pediatric_dose(${1:adult_dose_mg}, ${2:child_weight_kg})"),
    _fn("pediatric_bsa_dose", "pediatric_bsa_dose(adult_dose_mg, child_bsa_m2) -> float",
         f"**Pediatric BSA-based dose** (mg)\n\nFormula: `(child_BSA / 1.73) \u00d7 adult_dose`{_MED_DISCLAIMER}",
         snippet="pediatric_bsa_dose(${1:adult_dose_mg}, ${2:child_bsa_m2})"),
    _fn("pediatric_maintenance_fluid", "pediatric_maintenance_fluid(weight_kg) -> float",
         f"**Pediatric maintenance IV fluid** \u2014 Holliday-Segar (mL/24h)\n\n- First 10 kg: 100 mL/kg/day\n- Next 10 kg: 50 mL/kg/day\n- Each kg above 20: 20 mL/kg/day{_MED_DISCLAIMER}"),

    # Pharmacology
    _fn("dose_per_kg", "dose_per_kg(mg_per_kg, weight_kg) -> float",
         f"**Weight-based dose** (mg)\n\n```silk\ndose_per_kg(15.0, 25.0)  // 375.0\n```{_MED_DISCLAIMER}",
         snippet="dose_per_kg(${1:mg_per_kg}, ${2:weight_kg})"),
    _fn("dose_per_bsa", "dose_per_bsa(mg_per_m2, bsa_m2) -> float",
         f"**BSA-based dose** (mg)\n\nFormula: `mg_per_m\u00b2 \u00d7 BSA`{_MED_DISCLAIMER}",
         snippet="dose_per_bsa(${1:mg_per_m2}, ${2:bsa_m2})"),
    _fn("iv_drip_rate", "iv_drip_rate(volume_mL, time_hours, drop_factor) -> float",
         f"**IV drip rate** (drops/min)\n\nFormula: `(volume \u00d7 drop_factor) / (time \u00d7 60)`{_MED_DISCLAIMER}",
         snippet="iv_drip_rate(${1:volume_mL}, ${2:time_hours}, ${3:drop_factor})"),
    _fn("concentration", "concentration(amount_mg, volume_mL) -> float",
         f"**Drug concentration** (mg/mL)\n\nFormula: `amount / volume`{_MED_DISCLAIMER}",
         snippet="concentration(${1:amount_mg}, ${2:volume_mL})"),
    _fn("dilution", "dilution(c1, v1, c2) -> float",
         f"**Dilution** \u2014 C1V1 = C2V2\n\nReturns required final volume V2.\n\nFormula: `V2 = (C1 \u00d7 V1) / C2`{_MED_DISCLAIMER}",
         snippet="dilution(${1:c1}, ${2:v1}, ${3:c2})"),

    # Temperature
    _fn("celsius_to_fahrenheit", "celsius_to_fahrenheit(celsius) -> float",
         "Convert Celsius to Fahrenheit.\n\nFormula: `(C \u00d7 9/5) + 32`\n\n```silk\ncelsius_to_fahrenheit(37.0)  // 98.6\n```"),
    _fn("fahrenheit_to_celsius", "fahrenheit_to_celsius(fahrenheit) -> float",
         "Convert Fahrenheit to Celsius.\n\nFormula: `(F - 32) \u00d7 5/9`\n\n```silk\nfahrenheit_to_celsius(98.6)  // 37.0\n```"),

    # Cardiovascular
    _fn("map_pressure", "map_pressure(systolic, diastolic) -> float",
         f"**Mean Arterial Pressure** (mmHg)\n\nFormula: `diastolic + (systolic - diastolic) / 3`{_MED_DISCLAIMER}",
         snippet="map_pressure(${1:systolic}, ${2:diastolic})"),
    _fn("corrected_qt", "corrected_qt(qt_ms, rr_ms) -> float",
         f"**Corrected QT interval** \u2014 Bazett's formula (ms)\n\nFormula: `QT / sqrt(RR / 1000)`{_MED_DISCLAIMER}",
         snippet="corrected_qt(${1:qt_ms}, ${2:rr_ms})"),

    # Lab Values
    _fn("anion_gap", "anion_gap(sodium, chloride, bicarb) -> float",
         f"**Serum Anion Gap** (mEq/L)\n\nFormula: `Na - (Cl + HCO3)`\nNormal range: 8\u201312 mEq/L{_MED_DISCLAIMER}",
         snippet="anion_gap(${1:sodium}, ${2:chloride}, ${3:bicarb})"),
    _fn("corrected_sodium", "corrected_sodium(sodium, glucose) -> float",
         f"**Corrected Sodium** for hyperglycemia (mEq/L)\n\nFormula: `Na + 1.6 \u00d7 ((glucose - 100) / 100)`{_MED_DISCLAIMER}",
         snippet="corrected_sodium(${1:sodium}, ${2:glucose})"),
    _fn("corrected_calcium", "corrected_calcium(calcium, albumin) -> float",
         f"**Corrected Calcium** for low albumin (mg/dL)\n\nFormula: `calcium + 0.8 \u00d7 (4.0 - albumin)`{_MED_DISCLAIMER}",
         snippet="corrected_calcium(${1:calcium}, ${2:albumin})"),

    # Statistics
    _fn("mean", "mean(array) -> float", "Arithmetic mean of an array."),
    _fn("median", "median(array) -> float", "Median of an array."),
    _fn("stdev", "stdev(array) -> float", "Sample standard deviation of an array."),
]


def get_all_completions() -> list[CompletionItem]:
    """Return all completion items for the Silk language."""
    return (
        KEYWORD_ITEMS
        + CORE_FUNCTION_ITEMS
        + CONSTRUCTOR_ITEMS
        + MATH_FUNCTION_ITEMS
        + MEDICAL_FUNCTION_ITEMS
    )
