"""
Tests for string .toDoublePipeDelimited() method - split words by ||.
"""

from silk.interpreter import Interpreter


class TestStringToDoublePipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoublePipeDelimited_basic(self):
        output = self._run('print("hello world".toDoublePipeDelimited())')
        assert output[-1] == "hello||world"

    def test_toDoublePipeDelimited_three(self):
        output = self._run('print("a b c".toDoublePipeDelimited())')
        assert output[-1] == "a||b||c"
