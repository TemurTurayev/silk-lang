"""
Tests for string .wrapEach(before, after) method.
"""

from silk.interpreter import Interpreter


class TestStringWrapEach:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_wrapEach_basic(self):
        output = self._run('print("abc".wrapEach("[", "]"))')
        assert output[-1] == "[a][b][c]"

    def test_wrapEach_spaces(self):
        output = self._run('print("hi".wrapEach("<", ">"))')
        assert output[-1] == "<h><i>"
