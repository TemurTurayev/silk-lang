"""
Tests for number .digitTripleSum() method - sum of each consecutive triple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTripleSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTripleSum_basic(self):
        output = self._run('print(123456.digitTripleSum())')
        # [1+2+3=6, 4+5+6=15]
        assert output[-1] == "[6, 15]"

    def test_digitTripleSum_remainder(self):
        output = self._run('print(12345.digitTripleSum())')
        # [1+2+3=6, 4+5=9]
        assert output[-1] == "[6, 9]"
