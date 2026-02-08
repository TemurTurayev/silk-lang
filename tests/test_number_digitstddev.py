"""
Tests for number .digitStdDev() method - standard deviation of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitStdDev:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitStdDev_equal(self):
        output = self._run('print(333.digitStdDev())')
        assert output[-1] == "0"

    def test_digitStdDev_varied(self):
        output = self._run('print(13.digitStdDev())')
        assert output[-1] == "1"
