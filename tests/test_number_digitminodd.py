"""
Tests for number .digitMinOdd() method - smallest odd digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMinOdd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMinOdd_basic(self):
        output = self._run('print(1357.digitMinOdd())')
        assert output[-1] == "1"

    def test_digitMinOdd_mixed(self):
        output = self._run('print(2395.digitMinOdd())')
        assert output[-1] == "3"
