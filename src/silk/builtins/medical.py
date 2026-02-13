"""
Silk Medical Built-in Functions

Medical calculations and utilities.

⚠️ IMPORTANT DISCLAIMER:
These functions perform CALCULATIONS only.
They do NOT provide medical advice or diagnoses.
All results require clinical interpretation by a qualified healthcare professional.
"""

import math
from typing import Callable


def _median(arr: list) -> float:
    """Calculate median of a list."""
    s = sorted(arr)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2


def _stdev(arr: list) -> float:
    """Calculate sample standard deviation."""
    n = len(arr)
    if n < 2:
        return 0.0
    m = sum(arr) / n
    variance = sum((x - m) ** 2 for x in arr) / (n - 1)
    return round(math.sqrt(variance), 4)


# ═══════════════════════════════════════════════════════════
# ANTHROPOMETRIC CALCULATIONS
# ═══════════════════════════════════════════════════════════

def builtin_bmi(args: list, context: dict) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms
        height_m: Height in meters

    Returns:
        BMI value rounded to 2 decimal places

    Formula: weight / height²
    """
    weight_kg, height_m = args[0], args[1]
    return round(weight_kg / (height_m ** 2), 2)


def builtin_bsa(args: list, context: dict) -> float:
    """
    Calculate Body Surface Area (BSA) using Du Bois formula.

    Args:
        weight_kg: Weight in kilograms
        height_cm: Height in centimeters

    Returns:
        BSA in m² rounded to 2 decimal places

    Formula: 0.007184 × weight^0.425 × height^0.725
    """
    weight_kg, height_cm = args[0], args[1]
    return round(0.007184 * (weight_kg ** 0.425) * (height_cm ** 0.725), 2)


def builtin_ideal_body_weight(args: list, context: dict) -> float:
    """
    Calculate Ideal Body Weight (IBW) using Devine formula.

    Args:
        height_cm: Height in centimeters
        is_male: Boolean (true for male, false for female)

    Returns:
        IBW in kg rounded to 1 decimal place

    Formula:
        Male: 50 + 0.91 × (height_cm - 152.4)
        Female: 45.5 + 0.91 × (height_cm - 152.4)
    """
    height_cm, is_male = args[0], args[1]
    if is_male:
        return round(50 + 0.91 * (height_cm - 152.4), 1)
    else:
        return round(45.5 + 0.91 * (height_cm - 152.4), 1)


# ═══════════════════════════════════════════════════════════
# DOSING CALCULATIONS
# ═══════════════════════════════════════════════════════════

def builtin_dose_per_kg(args: list, context: dict) -> float:
    """
    Calculate dose based on weight.

    Args:
        mg_per_kg: Dose in mg per kg body weight
        weight_kg: Patient weight in kg

    Returns:
        Total dose in mg rounded to 2 decimal places
    """
    mg_per_kg, weight_kg = args[0], args[1]
    return round(mg_per_kg * weight_kg, 2)


# ═══════════════════════════════════════════════════════════
# TEMPERATURE CONVERSION
# ═══════════════════════════════════════════════════════════

def builtin_celsius_to_fahrenheit(args: list, context: dict) -> float:
    """
    Convert Celsius to Fahrenheit.

    Formula: (C × 9/5) + 32
    """
    celsius = args[0]
    return round(celsius * 9 / 5 + 32, 2)


def builtin_fahrenheit_to_celsius(args: list, context: dict) -> float:
    """
    Convert Fahrenheit to Celsius.

    Formula: (F - 32) × 5/9
    """
    fahrenheit = args[0]
    return round((fahrenheit - 32) * 5 / 9, 2)


# ═══════════════════════════════════════════════════════════
# STATISTICAL CALCULATIONS
# ═══════════════════════════════════════════════════════════

def builtin_mean(args: list, context: dict) -> float | None:
    """
    Calculate arithmetic mean of an array.
    """
    if isinstance(args[0], list) and len(args[0]) > 0:
        return round(sum(args[0]) / len(args[0]), 4)
    return None


def builtin_median(args: list, context: dict) -> float | None:
    """
    Calculate median of an array.
    """
    if isinstance(args[0], list) and len(args[0]) > 0:
        return _median(args[0])
    return None


def builtin_stdev(args: list, context: dict) -> float | None:
    """
    Calculate sample standard deviation of an array.
    """
    if isinstance(args[0], list) and len(args[0]) > 1:
        return _stdev(args[0])
    return None


# ═══════════════════════════════════════════════════════════
# RENAL FUNCTION
# ═══════════════════════════════════════════════════════════

def builtin_creatinine_clearance(args: list, context: dict) -> float:
    """
    Estimate creatinine clearance using Cockcroft-Gault equation.

    Args:
        age: Age in years
        weight_kg: Weight in kilograms
        creatinine: Serum creatinine in mg/dL
        is_male: Boolean (true for male, false for female)

    Returns:
        CrCl in mL/min rounded to 1 decimal place

    Formula: ((140 - age) × weight) / (72 × creatinine) [× 0.85 if female]
    """
    from ..errors import RuntimeError_
    age, weight, creatinine, is_male = args[0], args[1], args[2], args[3]
    if creatinine <= 0:
        raise RuntimeError_("Serum creatinine must be positive")
    result = ((140 - age) * weight) / (72 * creatinine)
    if not is_male:
        result *= 0.85
    return round(result, 1)


def builtin_egfr(args: list, context: dict) -> float:
    """
    Estimate GFR using CKD-EPI 2021 equation (race-free).

    Args:
        creatinine: Serum creatinine in mg/dL
        age: Age in years
        is_male: Boolean

    Returns:
        eGFR in mL/min/1.73m² rounded to 1 decimal place
    """
    creatinine, age, is_male = args[0], args[1], args[2]
    if is_male:
        kappa = 0.9
        alpha = -0.302 if creatinine <= kappa else -1.200
    else:
        kappa = 0.7
        alpha = -0.241 if creatinine <= kappa else -1.200

    a_coeff = 142
    min_cr = min(creatinine / kappa, 1.0)
    max_cr = max(creatinine / kappa, 1.0)
    result = a_coeff * (min_cr ** alpha) * (max_cr ** -1.200) * (0.9938 ** age)
    if not is_male:
        result *= 1.012
    return round(result, 1)


# ═══════════════════════════════════════════════════════════
# PEDIATRIC CALCULATIONS
# ═══════════════════════════════════════════════════════════

def builtin_pediatric_dose(args: list, context: dict) -> float:
    """
    Calculate pediatric dose using Clark's rule.

    Args:
        adult_dose_mg: Standard adult dose in mg
        child_weight_kg: Child's weight in kg

    Returns:
        Pediatric dose in mg rounded to 2 decimal places

    Formula: (child_weight / 70) × adult_dose
    """
    adult_dose, child_weight = args[0], args[1]
    return round((child_weight / 70) * adult_dose, 2)


def builtin_pediatric_bsa_dose(args: list, context: dict) -> float:
    """
    Calculate pediatric dose using BSA-based method.

    Args:
        adult_dose_mg: Standard adult dose in mg
        child_bsa_m2: Child's BSA in m²

    Returns:
        Pediatric dose in mg rounded to 2 decimal places

    Formula: (child_BSA / 1.73) × adult_dose
    """
    adult_dose, child_bsa = args[0], args[1]
    return round((child_bsa / 1.73) * adult_dose, 2)


def builtin_pediatric_maintenance_fluid(args: list, context: dict) -> float:
    """
    Calculate pediatric maintenance IV fluid rate (Holliday-Segar formula).

    Args:
        weight_kg: Child's weight in kg

    Returns:
        mL per 24 hours

    Formula:
        First 10 kg: 100 mL/kg/day
        Next 10 kg: 50 mL/kg/day
        Each kg above 20: 20 mL/kg/day
    """
    weight = args[0]
    if weight <= 10:
        return round(weight * 100, 1)
    elif weight <= 20:
        return round(1000 + (weight - 10) * 50, 1)
    else:
        return round(1500 + (weight - 20) * 20, 1)


# ═══════════════════════════════════════════════════════════
# PHARMACOLOGY
# ═══════════════════════════════════════════════════════════

def builtin_dose_per_bsa(args: list, context: dict) -> float:
    """
    Calculate dose based on body surface area.

    Args:
        mg_per_m2: Dose in mg per m² BSA
        bsa_m2: Patient BSA in m²

    Returns:
        Total dose in mg rounded to 2 decimal places
    """
    mg_per_m2, bsa = args[0], args[1]
    return round(mg_per_m2 * bsa, 2)


def builtin_iv_drip_rate(args: list, context: dict) -> float:
    """
    Calculate IV drip rate in drops per minute.

    Args:
        volume_ml: Total volume to infuse in mL
        time_hours: Duration in hours
        drop_factor: Drops per mL (typically 10, 15, or 20)

    Returns:
        Drops per minute rounded to 1 decimal place

    Formula: (volume × drop_factor) / (time × 60)
    """
    from ..errors import RuntimeError_
    volume, time_hours, drop_factor = args[0], args[1], args[2]
    if time_hours <= 0:
        raise RuntimeError_("Infusion time must be positive")
    return round((volume * drop_factor) / (time_hours * 60), 1)


def builtin_concentration(args: list, context: dict) -> float:
    """
    Calculate drug concentration.

    Args:
        amount_mg: Amount of drug in mg
        volume_ml: Volume of solution in mL

    Returns:
        Concentration in mg/mL rounded to 4 decimal places
    """
    from ..errors import RuntimeError_
    amount, volume = args[0], args[1]
    if volume <= 0:
        raise RuntimeError_("Volume must be positive")
    return round(amount / volume, 4)


def builtin_dilution(args: list, context: dict) -> float:
    """
    Calculate dilution using C1V1 = C2V2.

    Args:
        c1: Initial concentration
        v1: Initial volume
        c2: Desired concentration

    Returns:
        Required final volume (V2) rounded to 2 decimal places

    Formula: V2 = (C1 × V1) / C2
    """
    from ..errors import RuntimeError_
    c1, v1, c2 = args[0], args[1], args[2]
    if c2 <= 0:
        raise RuntimeError_("Target concentration must be positive")
    return round((c1 * v1) / c2, 2)


# ═══════════════════════════════════════════════════════════
# CARDIOVASCULAR
# ═══════════════════════════════════════════════════════════

def builtin_map_pressure(args: list, context: dict) -> float:
    """
    Calculate Mean Arterial Pressure (MAP).

    Args:
        systolic: Systolic blood pressure (mmHg)
        diastolic: Diastolic blood pressure (mmHg)

    Returns:
        MAP in mmHg rounded to 1 decimal place

    Formula: diastolic + (systolic - diastolic) / 3
    """
    systolic, diastolic = args[0], args[1]
    return round(diastolic + (systolic - diastolic) / 3, 1)


def builtin_corrected_qt(args: list, context: dict) -> float:
    """
    Calculate corrected QT interval using Bazett's formula.

    Args:
        qt_ms: QT interval in milliseconds
        rr_ms: RR interval in milliseconds

    Returns:
        QTc in milliseconds rounded to 1 decimal place

    Formula: QT / sqrt(RR/1000)
    """
    from ..errors import RuntimeError_
    qt, rr = args[0], args[1]
    if rr <= 0:
        raise RuntimeError_("RR interval must be positive")
    return round(qt / math.sqrt(rr / 1000), 1)


# ═══════════════════════════════════════════════════════════
# LAB VALUES
# ═══════════════════════════════════════════════════════════

def builtin_anion_gap(args: list, context: dict) -> float:
    """
    Calculate serum anion gap.

    Args:
        sodium: Na+ in mEq/L
        chloride: Cl- in mEq/L
        bicarb: HCO3- in mEq/L

    Returns:
        Anion gap in mEq/L

    Formula: Na - (Cl + HCO3)
    Normal range: 8-12 mEq/L
    """
    na, cl, bicarb = args[0], args[1], args[2]
    return round(na - (cl + bicarb), 1)


def builtin_corrected_sodium(args: list, context: dict) -> float:
    """
    Calculate corrected sodium for hyperglycemia.

    Args:
        sodium: Measured sodium in mEq/L
        glucose: Blood glucose in mg/dL

    Returns:
        Corrected sodium in mEq/L rounded to 1 decimal place

    Formula: Na + 1.6 × ((glucose - 100) / 100)
    """
    na, glucose = args[0], args[1]
    return round(na + 1.6 * ((glucose - 100) / 100), 1)


def builtin_corrected_calcium(args: list, context: dict) -> float:
    """
    Calculate corrected calcium for low albumin.

    Args:
        calcium: Total calcium in mg/dL
        albumin: Serum albumin in g/dL

    Returns:
        Corrected calcium in mg/dL rounded to 1 decimal place

    Formula: calcium + 0.8 × (4.0 - albumin)
    """
    calcium, albumin = args[0], args[1]
    return round(calcium + 0.8 * (4.0 - albumin), 1)


def builtin_bmi_category(args: list, context: dict) -> str:
    """
    Return BMI category as a string.

    Args:
        bmi_value: BMI number

    Returns:
        Category string: "underweight", "normal", "overweight", "obese"
    """
    bmi_val = args[0]
    if bmi_val < 18.5:
        return "underweight"
    elif bmi_val < 25:
        return "normal"
    elif bmi_val < 30:
        return "overweight"
    else:
        return "obese"


# Export all medical built-ins
MEDICAL_BUILTINS: dict[str, Callable] = {
    # Anthropometric
    'bmi': builtin_bmi,
    'bsa': builtin_bsa,
    'ideal_body_weight': builtin_ideal_body_weight,
    'bmi_category': builtin_bmi_category,

    # Renal
    'creatinine_clearance': builtin_creatinine_clearance,
    'egfr': builtin_egfr,

    # Pediatric
    'pediatric_dose': builtin_pediatric_dose,
    'pediatric_bsa_dose': builtin_pediatric_bsa_dose,
    'pediatric_maintenance_fluid': builtin_pediatric_maintenance_fluid,

    # Dosing / Pharmacology
    'dose_per_kg': builtin_dose_per_kg,
    'dose_per_bsa': builtin_dose_per_bsa,
    'iv_drip_rate': builtin_iv_drip_rate,
    'concentration': builtin_concentration,
    'dilution': builtin_dilution,

    # Temperature
    'celsius_to_fahrenheit': builtin_celsius_to_fahrenheit,
    'fahrenheit_to_celsius': builtin_fahrenheit_to_celsius,

    # Cardiovascular
    'map_pressure': builtin_map_pressure,
    'corrected_qt': builtin_corrected_qt,

    # Lab Values
    'anion_gap': builtin_anion_gap,
    'corrected_sodium': builtin_corrected_sodium,
    'corrected_calcium': builtin_corrected_calcium,

    # Statistics
    'mean': builtin_mean,
    'median': builtin_median,
    'stdev': builtin_stdev,
}
