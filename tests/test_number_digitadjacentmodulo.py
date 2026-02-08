"""
Tests for number .digitAdjacentModulo() method - modulo of adjacent digit pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentModulo:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentModulo_basic(self):
        output = self._run('print(573.digitAdjacentModulo())')
        # 5%7, 7%3 = [5, 1]
        assert output[-1] == "[5, 1]"

    def test_digitAdjacentModulo_even(self):
        output = self._run('print(842.digitAdjacentModulo())')
        # 8%4, 4%2 = [0, 0]
        assert output[-1] == "[0, 0]"
