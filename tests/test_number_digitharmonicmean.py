"""
Tests for number .digitHarmonicMean() method - harmonic mean of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitHarmonicMean:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitHarmonicMean_equal(self):
        output = self._run('print(333.digitHarmonicMean())')
        assert output[-1] == "3"

    def test_digitHarmonicMean_varied(self):
        output = self._run('print(24.digitHarmonicMean())')
        # HM(2,4) = 2 / (1/2 + 1/4) = 2 / 0.75 = 2.6666...
        assert output[-1].startswith("2.6")
