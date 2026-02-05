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


# Export all medical built-ins
MEDICAL_BUILTINS: dict[str, Callable] = {
    # Anthropometric
    'bmi': builtin_bmi,
    'bsa': builtin_bsa,
    'ideal_body_weight': builtin_ideal_body_weight,

    # Dosing
    'dose_per_kg': builtin_dose_per_kg,

    # Temperature
    'celsius_to_fahrenheit': builtin_celsius_to_fahrenheit,
    'fahrenheit_to_celsius': builtin_fahrenheit_to_celsius,

    # Statistics
    'mean': builtin_mean,
    'median': builtin_median,
    'stdev': builtin_stdev,
}
