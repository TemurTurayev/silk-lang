"""Tests for the unit type — physical unit safety for medical calculations."""

import sys
import pytest
sys.path.insert(0, 'src')

from silk import Interpreter


class TestUnitCreation:
    """Test creating unit values."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_create_mg(self):
        out = self._run('print(unit(500, "mg"))')
        assert out == ["500 mg"]

    def test_create_kg(self):
        out = self._run('print(unit(70, "kg"))')
        assert out == ["70 kg"]

    def test_create_ml(self):
        out = self._run('print(unit(1.5, "mL"))')
        assert out == ["1.5 mL"]

    def test_type_name(self):
        out = self._run('print(type(unit(10, "mg")))')
        assert out == ["unit"]

    def test_unknown_unit_error(self):
        interp = Interpreter()
        result = interp.run('let x = unit(10, "xyz")')
        assert result is False


class TestUnitSafety:
    """Test that incompatible units produce errors."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def _fails(self, source):
        interp = Interpreter()
        return interp.run(source) is False

    def test_mg_plus_ml_error(self):
        """The killer feature: mass + volume must fail."""
        assert self._fails('''
let dose = unit(10, "mg")
let volume = unit(5, "mL")
let bad = dose + volume
''')

    def test_mg_plus_kg_ok(self):
        """Same dimension (mass) should work."""
        out = self._run('''
let a = unit(500, "mg")
let b = unit(1, "g")
print(a + b)
''')
        assert out == ["1500 mg"]

    def test_ml_plus_l_ok(self):
        """Same dimension (volume) should work."""
        out = self._run('''
let a = unit(500, "mL")
let b = unit(1, "L")
print(a + b)
''')
        assert out == ["1500 mL"]

    def test_subtract_same_unit(self):
        out = self._run('''
let a = unit(100, "mg")
let b = unit(30, "mg")
print(a - b)
''')
        assert out == ["70 mg"]

    def test_subtract_different_dimension_error(self):
        assert self._fails('''
let a = unit(100, "mg")
let b = unit(5, "mL")
let bad = a - b
''')


class TestUnitArithmetic:
    """Test arithmetic on units."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_multiply_by_scalar(self):
        out = self._run('''
let dose = unit(15, "mg")
print(dose * 3)
''')
        assert out == ["45 mg"]

    def test_scalar_multiply(self):
        out = self._run('''
let dose = unit(15, "mg")
print(2 * dose)
''')
        assert out == ["30 mg"]

    def test_divide_by_scalar(self):
        out = self._run('''
let total = unit(300, "mg")
print(total / 3)
''')
        assert out == ["100 mg"]

    def test_divide_same_dimension(self):
        """Dividing same-dimension units gives a scalar."""
        out = self._run('''
let a = unit(500, "mg")
let b = unit(250, "mg")
print(a / b)
''')
        assert out == ["2"]

    def test_negate(self):
        out = self._run('''
let x = unit(5, "mg")
print(-x)
''')
        assert out == ["-5 mg"]


class TestUnitComparison:
    """Test comparison between units."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_eq_same(self):
        out = self._run('print(unit(500, "mg") == unit(500, "mg"))')
        assert out == ["true"]

    def test_eq_converted(self):
        out = self._run('print(unit(1000, "mg") == unit(1, "g"))')
        assert out == ["true"]

    def test_neq(self):
        out = self._run('print(unit(100, "mg") != unit(200, "mg"))')
        assert out == ["true"]

    def test_lt(self):
        out = self._run('print(unit(100, "mg") < unit(200, "mg"))')
        assert out == ["true"]

    def test_gt(self):
        out = self._run('print(unit(200, "mg") > unit(100, "mg"))')
        assert out == ["true"]


class TestUnitMembers:
    """Test unit member access and methods."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_value(self):
        out = self._run('print(unit(500, "mg").value)')
        assert out == ["500"]

    def test_unit_name(self):
        out = self._run('print(unit(500, "mg").unit)')
        assert out == ["mg"]

    def test_dimension(self):
        out = self._run('print(unit(500, "mg").dimension)')
        assert out == ["mass"]

    def test_convert_to(self):
        out = self._run('''
let dose = unit(1500, "mg")
print(dose.convertTo("g"))
''')
        assert out == ["1.5 g"]

    def test_convert_incompatible_error(self):
        interp = Interpreter()
        result = interp.run('''
let dose = unit(500, "mg")
let bad = dose.convertTo("mL")
''')
        assert result is False

    def test_round(self):
        out = self._run('''
let rate = unit(41.6667, "mL")
print(rate.round(1))
''')
        assert out == ["41.7 mL"]

    def test_abs(self):
        out = self._run('print(unit(-5, "mg").abs())')
        assert out == ["5 mg"]


class TestUnitMedicalScenarios:
    """Real-world medical use cases."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def _fails(self, source):
        interp = Interpreter()
        return interp.run(source) is False

    def test_weight_based_dosing(self):
        """Calculate dose: mg/kg * weight."""
        out = self._run('''
let dose_per_kg = 15
let weight = unit(25, "kg")
let total_dose = unit(dose_per_kg * weight.value, "mg")
print(total_dose)
''')
        assert out == ["375 mg"]

    def test_unit_conversion_chain(self):
        """Convert g -> mg for dosing."""
        out = self._run('''
let drug = unit(2, "g")
let in_mg = drug.convertTo("mg")
print(in_mg)
''')
        assert out == ["2000 mg"]

    def test_prevent_dosing_error(self):
        """Cannot add mg to mL — catches dangerous mistakes."""
        assert self._fails('''
let drug_amount = unit(500, "mg")
let fluid_volume = unit(100, "mL")
let wrong = drug_amount + fluid_volume
''')

    def test_time_conversion(self):
        out = self._run('''
let duration = unit(2, "hr")
let in_min = duration.convertTo("min")
print(in_min)
''')
        assert out == ["120 min"]

    def test_concentration_division(self):
        """mg / mL gives mg/mL concentration."""
        out = self._run('''
let amount = unit(500, "mg")
let volume = unit(10, "mL")
let conc = amount / volume
print(conc)
''')
        assert out == ["50 mg/mL"]
