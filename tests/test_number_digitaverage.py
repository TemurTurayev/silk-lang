"""
Tests for number .digitAverage() method - average of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAverage:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAverage_basic(self):
        output = self._run('print(246.digitAverage())')
        assert output[-1] == "4"

    def test_digitAverage_decimal(self):
        output = self._run('print(123.digitAverage())')
        assert output[-1] == "2"
