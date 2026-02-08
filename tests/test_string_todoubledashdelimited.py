"""
Tests for string .toDoubleDashDelimited() method - split words by --.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleDashDelimited_basic(self):
        output = self._run('print("hello world".toDoubleDashDelimited())')
        assert output[-1] == "hello--world"

    def test_toDoubleDashDelimited_three(self):
        output = self._run('print("a b c".toDoubleDashDelimited())')
        assert output[-1] == "a--b--c"
