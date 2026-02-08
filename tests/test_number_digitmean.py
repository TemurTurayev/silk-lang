"""
Tests for number .digitMean() method - arithmetic mean of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMean:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMean_equal(self):
        output = self._run('print(333.digitMean())')
        assert output[-1] == "3"

    def test_digitMean_varied(self):
        output = self._run('print(24.digitMean())')
        assert output[-1] == "3"
