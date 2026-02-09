"""
Tests for string .toOctodecColonDelimited() method - join words with 18 colons.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecColonDelimited_basic(self):
        output = self._run('print("hello world".toOctodecColonDelimited())')
        assert output[-1] == "hello" + ":" * 18 + "world"

    def test_toOctodecColonDelimited_three(self):
        output = self._run('print("a b c".toOctodecColonDelimited())')
        assert output[-1] == "a" + ":" * 18 + "b" + ":" * 18 + "c"
