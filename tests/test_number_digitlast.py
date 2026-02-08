"""
Tests for number .digitLast() method - return last digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitLast:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitLast_basic(self):
        output = self._run('print(12345.digitLast())')
        assert output[-1] == "5"

    def test_digitLast_single(self):
        output = self._run('print(7.digitLast())')
        assert output[-1] == "7"
