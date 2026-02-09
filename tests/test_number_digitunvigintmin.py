"""
Tests for number .digitUnvigintMin() method - min of each consecutive 21-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnvigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnvigintMin_basic(self):
        output = self._run('print(121112111211121112111.digitUnvigintMin())')
        assert output[-1] == "[1]"

    def test_digitUnvigintMin_remainder(self):
        output = self._run('print(1211121112111211121119.digitUnvigintMin())')
        # min(...)=1, min(9)=9
        assert output[-1] == "[1, 9]"
