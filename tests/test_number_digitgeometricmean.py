"""
Tests for number .digitGeometricMean() method - geometric mean of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitGeometricMean:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitGeometricMean_equal(self):
        output = self._run('print(333.digitGeometricMean())')
        assert output[-1] == "3"

    def test_digitGeometricMean_varied(self):
        output = self._run('print(28.digitGeometricMean())')
        assert output[-1] == "4"
