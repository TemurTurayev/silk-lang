"""
Tests for number .digitMaxOdd() method - largest odd digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMaxOdd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMaxOdd_basic(self):
        output = self._run('print(1357.digitMaxOdd())')
        assert output[-1] == "7"

    def test_digitMaxOdd_mixed(self):
        output = self._run('print(1234.digitMaxOdd())')
        assert output[-1] == "3"
