"""
Tests for string .centerPad(width, char) method.
"""

from silk.interpreter import Interpreter


class TestStringCenterPad:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_centerPad_basic(self):
        output = self._run('print("hi".centerPad(6, "-"))')
        assert output[-1] == "--hi--"

    def test_centerPad_no_change(self):
        output = self._run('print("hello".centerPad(3, "*"))')
        assert output[-1] == "hello"
