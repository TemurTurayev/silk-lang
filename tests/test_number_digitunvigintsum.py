"""
Tests for number .digitUnvigintSum() method - sum of each consecutive 21-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnvigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnvigintSum_basic(self):
        output = self._run('print(111111111111111111111.digitUnvigintSum())')
        assert output[-1] == "[21]"

    def test_digitUnvigintSum_remainder(self):
        output = self._run('print(1111111111111111111115.digitUnvigintSum())')
        # sum(1*21)=21, sum(5)=5
        assert output[-1] == "[21, 5]"
