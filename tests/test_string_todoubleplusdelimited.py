"""
Tests for string .toDoublePlusDelimited() method - split words by ++.
"""

from silk.interpreter import Interpreter


class TestStringToDoublePlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoublePlusDelimited_basic(self):
        output = self._run('print("hello world".toDoublePlusDelimited())')
        assert output[-1] == "hello++world"

    def test_toDoublePlusDelimited_three(self):
        output = self._run('print("a b c".toDoublePlusDelimited())')
        assert output[-1] == "a++b++c"
