"""
Tests for number .digitCountOdd() method - count odd digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitCountOdd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitCountOdd_allOdd(self):
        output = self._run('print(1357.digitCountOdd())')
        assert output[-1] == "4"

    def test_digitCountOdd_mixed(self):
        output = self._run('print(12345.digitCountOdd())')
        assert output[-1] == "3"
