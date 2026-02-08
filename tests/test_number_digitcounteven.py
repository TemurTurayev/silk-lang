"""
Tests for number .digitCountEven() method - count even digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitCountEven:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitCountEven_allEven(self):
        output = self._run('print(2468.digitCountEven())')
        assert output[-1] == "4"

    def test_digitCountEven_mixed(self):
        output = self._run('print(12345.digitCountEven())')
        assert output[-1] == "2"
