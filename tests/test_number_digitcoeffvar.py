"""
Tests for number .digitCoeffVar() method - coefficient of variation of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitCoeffVar:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitCoeffVar_equal(self):
        output = self._run('print(333.digitCoeffVar())')
        assert output[-1] == "0"

    def test_digitCoeffVar_varied(self):
        output = self._run('print(24.digitCoeffVar())')
        # digits 2,4 => mean=3, std=1, CV=1/3=0.333...
        assert output[-1].startswith("0.3")
