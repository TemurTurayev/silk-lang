"""
Tests for number .digitMin() method - smallest digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMin_basic(self):
        output = self._run('print(5312.digitMin())')
        assert output[-1] == "1"

    def test_digitMin_with_zero(self):
        output = self._run('print(9071.digitMin())')
        assert output[-1] == "0"
