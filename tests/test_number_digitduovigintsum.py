"""
Tests for number .digitDuovigintSum() method - sum of each consecutive 22-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuovigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuovigintSum_basic(self):
        output = self._run('print(1111111111111111111111.digitDuovigintSum())')
        assert output[-1] == "[22]"

    def test_digitDuovigintSum_remainder(self):
        output = self._run('print(11111111111111111111113.digitDuovigintSum())')
        # sum(1*22)=22, sum(3)=3
        assert output[-1] == "[22, 3]"
