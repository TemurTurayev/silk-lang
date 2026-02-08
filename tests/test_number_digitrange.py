"""
Tests for number .digitRange() method - difference between max and min digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitRange:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitRange_basic(self):
        output = self._run('print(192.digitRange())')
        assert output[-1] == "8"

    def test_digitRange_same(self):
        output = self._run('print(555.digitRange())')
        assert output[-1] == "0"
