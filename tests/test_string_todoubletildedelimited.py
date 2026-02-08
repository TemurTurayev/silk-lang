"""
Tests for string .toDoubleTildeDelimited() method - split words by ~~.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleTildeDelimited_basic(self):
        output = self._run('print("hello world".toDoubleTildeDelimited())')
        assert output[-1] == "hello~~world"

    def test_toDoubleTildeDelimited_three(self):
        output = self._run('print("a b c".toDoubleTildeDelimited())')
        assert output[-1] == "a~~b~~c"
