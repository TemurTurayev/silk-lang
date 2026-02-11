"""
Tests for string .toUnvigintiColonDelimited() method - join words with 21 colons.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiColonDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiColonDelimited())')
        assert output[-1] == "hello" + ":" * 21 + "world"

    def test_toUnvigintiColonDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiColonDelimited())')
        assert output[-1] == "a" + ":" * 21 + "b" + ":" * 21 + "c"
