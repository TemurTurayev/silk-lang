"""Tests for extended medical stdlib functions."""

import sys
sys.path.insert(0, 'src')

from silk import Interpreter


class TestRenalFunctions:
    """Test renal function calculations."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_creatinine_clearance_male(self):
        out = self._run('print(creatinine_clearance(65, 70, 1.2, true))')
        assert out == ["60.8"]

    def test_creatinine_clearance_female(self):
        out = self._run('print(creatinine_clearance(65, 70, 1.2, false))')
        assert out == ["51.6"]

    def test_egfr_male(self):
        out = self._run('print(egfr(1.0, 50, true))')
        result = float(out[0])
        assert 80 < result < 110

    def test_egfr_female(self):
        out = self._run('print(egfr(1.0, 50, false))')
        result = float(out[0])
        assert 60 < result < 110


class TestPediatricFunctions:
    """Test pediatric calculations."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pediatric_dose(self):
        """Clark's rule: (25kg / 70) * 500mg = 178.57mg."""
        out = self._run('print(pediatric_dose(500, 25))')
        assert out == ["178.57"]

    def test_pediatric_bsa_dose(self):
        out = self._run('print(pediatric_bsa_dose(500, 0.8))')
        result = float(out[0])
        assert 200 < result < 250

    def test_maintenance_fluid_small(self):
        """< 10kg: 100 mL/kg/day -> 8kg = 800."""
        out = self._run('print(pediatric_maintenance_fluid(8))')
        assert out == ["800"]

    def test_maintenance_fluid_medium(self):
        """10-20kg: 1000 + 50*(weight-10) -> 15kg = 1250."""
        out = self._run('print(pediatric_maintenance_fluid(15))')
        assert out == ["1250"]

    def test_maintenance_fluid_large(self):
        """> 20kg: 1500 + 20*(weight-20) -> 30kg = 1700."""
        out = self._run('print(pediatric_maintenance_fluid(30))')
        assert out == ["1700"]


class TestPharmacologyFunctions:
    """Test pharmacology calculations."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_dose_per_bsa(self):
        out = self._run('print(dose_per_bsa(100, 1.73))')
        assert out == ["173"]

    def test_iv_drip_rate(self):
        """500mL / 4hr at 20 drops/mL = 41.7 drops/min."""
        out = self._run('print(iv_drip_rate(500, 4, 20))')
        assert out == ["41.7"]

    def test_concentration(self):
        out = self._run('print(concentration(500, 100))')
        assert out == ["5"]

    def test_dilution(self):
        """C1V1 = C2V2: 10 * 50 / 2 = 250."""
        out = self._run('print(dilution(10, 50, 2))')
        assert out == ["250"]


class TestCardiovascularFunctions:
    """Test cardiovascular calculations."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_map_pressure(self):
        """MAP = 80 + (120-80)/3 = 93.3."""
        out = self._run('print(map_pressure(120, 80))')
        assert out == ["93.3"]

    def test_corrected_qt(self):
        out = self._run('print(corrected_qt(400, 800))')
        result = float(out[0])
        assert 440 < result < 450


class TestLabValues:
    """Test lab value calculations."""

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_anion_gap(self):
        """AG = 140 - (100 + 24) = 16."""
        out = self._run('print(anion_gap(140, 100, 24))')
        assert out == ["16"]

    def test_corrected_sodium(self):
        """Na + 1.6 * ((glucose - 100) / 100)."""
        out = self._run('print(corrected_sodium(130, 500))')
        result = float(out[0])
        assert 136 < result < 137

    def test_corrected_calcium(self):
        """Ca + 0.8 * (4.0 - albumin)."""
        out = self._run('print(corrected_calcium(8.5, 2.0))')
        assert out == ["10.1"]

    def test_bmi_category(self):
        out = self._run('''
print(bmi_category(17))
print(bmi_category(22))
print(bmi_category(27))
print(bmi_category(35))
''')
        assert out == ["underweight", "normal", "overweight", "obese"]
