"""
Tests for string .toDotDelimited() method - split words by dot.
"""

from silk.interpreter import Interpreter


class TestStringToDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDotDelimited_basic(self):
        output = self._run('print("hello world".toDotDelimited())')
        assert output[-1] == "hello.world"

    def test_toDotDelimited_three(self):
        output = self._run('print("a b c".toDotDelimited())')
        assert output[-1] == "a.b.c"
