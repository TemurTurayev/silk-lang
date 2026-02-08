"""
Tests for number .digitMaxEven() method - largest even digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMaxEven:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMaxEven_basic(self):
        output = self._run('print(2468.digitMaxEven())')
        assert output[-1] == "8"

    def test_digitMaxEven_mixed(self):
        output = self._run('print(1234.digitMaxEven())')
        assert output[-1] == "4"
