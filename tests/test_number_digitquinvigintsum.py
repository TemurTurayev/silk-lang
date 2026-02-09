"""
Tests for number .digitQuinvigintSum() method - sum of each consecutive 25-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinvigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinvigintSum_basic(self):
        output = self._run('print(1111111111111111111111111.digitQuinvigintSum())')
        assert output[-1] == "[25]"

    def test_digitQuinvigintSum_remainder(self):
        output = self._run('print(11111111111111111111111113.digitQuinvigintSum())')
        assert output[-1] == "[25, 3]"
