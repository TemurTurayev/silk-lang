"""
Tests for number .digitTrevigintSum() method - sum of each consecutive 23-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrevigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrevigintSum_basic(self):
        output = self._run('print(11111111111111111111111.digitTrevigintSum())')
        assert output[-1] == "[23]"

    def test_digitTrevigintSum_remainder(self):
        output = self._run('print(111111111111111111111113.digitTrevigintSum())')
        # sum(1*23)=23, sum(3)=3
        assert output[-1] == "[23, 3]"
