"""
Tests for string .toUndecColonDelimited() method - split words by ::::::::::: (11 colons).
"""

from silk.interpreter import Interpreter


class TestStringToUndecColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecColonDelimited_basic(self):
        output = self._run('print("hello world".toUndecColonDelimited())')
        assert output[-1] == "hello:::::::::::world"

    def test_toUndecColonDelimited_three(self):
        output = self._run('print("a b c".toUndecColonDelimited())')
        assert output[-1] == "a:::::::::::b:::::::::::c"
