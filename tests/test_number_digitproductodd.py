"""
Tests for number .digitProductOdd() method - product of odd digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitProductOdd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitProductOdd_basic(self):
        output = self._run('print(1357.digitProductOdd())')
        # 1 * 3 * 5 * 7 = 105
        assert output[-1] == "105"

    def test_digitProductOdd_mixed(self):
        output = self._run('print(1234.digitProductOdd())')
        # odd digits: 1, 3 -> 1 * 3 = 3
        assert output[-1] == "3"
