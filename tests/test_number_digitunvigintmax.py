"""
Tests for number .digitUnvigintMax() method - max of each consecutive 21-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnvigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnvigintMax_basic(self):
        output = self._run('print(121112111211121112111.digitUnvigintMax())')
        assert output[-1] == "[2]"

    def test_digitUnvigintMax_remainder(self):
        output = self._run('print(1211121112111211121119.digitUnvigintMax())')
        # max(...)=2, max(9)=9
        assert output[-1] == "[2, 9]"
