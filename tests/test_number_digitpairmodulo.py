"""
Tests for number .digitPairModulo() method - modulo of each consecutive pair of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPairModulo:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPairModulo_basic(self):
        output = self._run('print(4268.digitPairModulo())')
        # [4%2=0, 6%8=6]
        assert output[-1] == "[0, 6]"

    def test_digitPairModulo_odd(self):
        output = self._run('print(93715.digitPairModulo())')
        # [9%3=0, 7%1=0, 5]
        assert output[-1] == "[0, 0, 5]"
