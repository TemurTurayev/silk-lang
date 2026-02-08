"""
Tests for string .toCenterPad(n) method - center pad string to length n.
"""

from silk.interpreter import Interpreter


class TestStringToCenterPad:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCenterPad_basic(self):
        output = self._run('print("hi".toCenterPad(6))')
        assert output[-1] == "  hi  "

    def test_toCenterPad_odd(self):
        output = self._run('print("hi".toCenterPad(7))')
        assert output[-1] == "   hi  "
