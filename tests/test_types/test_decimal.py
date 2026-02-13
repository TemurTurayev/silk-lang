"""Tests for the decimal type — precise arithmetic for medical dosing."""

import sys
sys.path.insert(0, 'src')

from silk import Interpreter


class TestDecimalCreation:
    """Test creating decimal values."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_decimal_from_string(self):
        out = self._run('print(decimal("0.1"))')
        assert out == ["0.1"]

    def test_decimal_from_int(self):
        out = self._run('print(decimal(42))')
        assert out == ["42"]

    def test_decimal_from_float(self):
        out = self._run('print(decimal(3.14))')
        assert out == ["3.14"]

    def test_decimal_type_name(self):
        out = self._run('print(type(decimal("1.5")))')
        assert out == ["decimal"]


class TestDecimalPrecision:
    """Test that decimal avoids float precision issues."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_point_one_plus_point_two(self):
        """The classic float bug: 0.1 + 0.2 should equal 0.3 exactly."""
        out = self._run('''
let a = decimal("0.1")
let b = decimal("0.2")
let c = a + b
print(c)
print(c == decimal("0.3"))
''')
        assert out == ["0.3", "true"]

    def test_dosing_precision(self):
        """Drug dosing must be exact: 15.75 mg/kg * 25 kg = 393.75 mg."""
        out = self._run('''
let mg_per_kg = decimal("15.75")
let weight = decimal("25")
let dose = mg_per_kg * weight
print(dose)
''')
        assert out == ["393.75"]

    def test_decimal_subtraction(self):
        out = self._run('''
let a = decimal("10.5")
let b = decimal("3.3")
print(a - b)
''')
        assert out == ["7.2"]

    def test_decimal_division(self):
        out = self._run('''
let a = decimal("10")
let b = decimal("3")
let result = a / b
print(result.round(4))
''')
        assert out == ["3.3333"]


class TestDecimalArithmetic:
    """Test all arithmetic operations on decimals."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_add(self):
        out = self._run('print(decimal("1.5") + decimal("2.5"))')
        assert out == ["4.0"]

    def test_sub(self):
        out = self._run('print(decimal("5.0") - decimal("2.3"))')
        assert out == ["2.7"]

    def test_mul(self):
        out = self._run('print(decimal("3.0") * decimal("2.5"))')
        assert out == ["7.50"]

    def test_div(self):
        out = self._run('print(decimal("10") / decimal("4"))')
        assert out == ["2.5"]

    def test_mod(self):
        out = self._run('print(decimal("10") % decimal("3"))')
        assert out == ["1"]

    def test_power(self):
        out = self._run('print(decimal("2") ** decimal("3"))')
        assert out == ["8"]

    def test_negate(self):
        out = self._run('''
let x = decimal("5.5")
print(-x)
''')
        assert out == ["-5.5"]


class TestDecimalComparison:
    """Test comparison operations."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_eq(self):
        out = self._run('print(decimal("1.0") == decimal("1.0"))')
        assert out == ["true"]

    def test_neq(self):
        out = self._run('print(decimal("1.0") != decimal("2.0"))')
        assert out == ["true"]

    def test_lt(self):
        out = self._run('print(decimal("1.0") < decimal("2.0"))')
        assert out == ["true"]

    def test_gt(self):
        out = self._run('print(decimal("2.0") > decimal("1.0"))')
        assert out == ["true"]

    def test_lte(self):
        out = self._run('print(decimal("1.0") <= decimal("1.0"))')
        assert out == ["true"]

    def test_gte(self):
        out = self._run('print(decimal("2.0") >= decimal("1.0"))')
        assert out == ["true"]

    def test_decimal_eq_int(self):
        out = self._run('print(decimal("5") == 5)')
        assert out == ["true"]


class TestDecimalMethods:
    """Test decimal member methods."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_round(self):
        out = self._run('print(decimal("3.14159").round(2))')
        assert out == ["3.14"]

    def test_round_zero(self):
        out = self._run('print(decimal("3.7").round(0))')
        assert out == ["4"]

    def test_abs(self):
        out = self._run('print(decimal("-5.5").abs())')
        assert out == ["5.5"]

    def test_to_int(self):
        out = self._run('print(decimal("3.7").toInt())')
        assert out == ["3"]

    def test_to_float(self):
        out = self._run('''
let x = decimal("3.14")
let f = x.toFloat()
print(type(f))
''')
        assert out == ["float"]

    def test_is_zero(self):
        out = self._run('print(decimal("0").isZero())')
        assert out == ["true"]

    def test_is_positive(self):
        out = self._run('print(decimal("5").isPositive())')
        assert out == ["true"]

    def test_is_negative(self):
        out = self._run('print(decimal("-3").isNegative())')
        assert out == ["true"]

    def test_negate_method(self):
        out = self._run('print(decimal("5.5").negate())')
        assert out == ["-5.5"]


class TestDecimalMixedArithmetic:
    """Test decimal with int/float operands."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_decimal_plus_int(self):
        out = self._run('print(decimal("1.5") + 2)')
        assert out == ["3.5"]

    def test_int_plus_decimal(self):
        out = self._run('print(2 + decimal("1.5"))')
        assert out == ["3.5"]

    def test_decimal_times_int(self):
        out = self._run('print(decimal("2.5") * 4)')
        assert out == ["10.0"]

    def test_decimal_conversion_from_int(self):
        out = self._run('''
let x = int(decimal("7.9"))
print(x)
print(type(x))
''')
        assert out == ["7", "int"]

    def test_decimal_conversion_from_float(self):
        out = self._run('''
let x = float(decimal("3.14"))
print(type(x))
''')
        assert out == ["float"]


class TestDecimalMedicalScenarios:
    """Real-world medical use cases."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_iv_drip_rate(self):
        """Calculate IV drip rate: volume / time * drop_factor."""
        out = self._run('''
let volume_ml = decimal("500")
let time_hours = decimal("4")
let drop_factor = decimal("20")
let rate = volume_ml / time_hours * drop_factor / decimal("60")
print(rate.round(1))
''')
        assert out == ["41.7"]

    def test_creatinine_clearance(self):
        """Cockcroft-Gault formula simplified check."""
        out = self._run('''
let age = decimal("65")
let weight = decimal("70")
let creatinine = decimal("1.2")
let factor = decimal("140") - age
let numerator = factor * weight
let denominator = decimal("72") * creatinine
let crcl = numerator / denominator
print(crcl.round(1))
''')
        assert out == ["60.8"]

    def test_bmi_precise(self):
        """BMI with decimal precision."""
        out = self._run('''
let weight = decimal("72.5")
let height = decimal("1.75")
let bmi_val = weight / (height * height)
print(bmi_val.round(2))
''')
        assert out == ["23.67"]
