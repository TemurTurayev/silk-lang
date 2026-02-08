"""
Tests for string .toTapCode() method - convert to tap code (Polybius cipher).
"""

from silk.interpreter import Interpreter


class TestStringToTapCode:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTapCode_hi(self):
        output = self._run('print("hi".toTapCode())')
        assert output[-1] == "2,3 2,4"

    def test_toTapCode_ab(self):
        output = self._run('print("ab".toTapCode())')
        assert output[-1] == "1,1 1,2"
