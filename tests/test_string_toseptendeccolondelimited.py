"""
Tests for string .toSeptendecColonDelimited() method - join words with 17 colons.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecColonDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecColonDelimited())')
        assert output[-1] == "hello" + ":" * 17 + "world"

    def test_toSeptendecColonDelimited_three(self):
        output = self._run('print("a b c".toSeptendecColonDelimited())')
        assert output[-1] == "a" + ":" * 17 + "b" + ":" * 17 + "c"
