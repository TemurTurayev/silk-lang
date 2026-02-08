"""
Tests for string .toNonColonDelimited() method - split words by ::::::::: (9 colons).
"""

from silk.interpreter import Interpreter


class TestStringToNonColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonColonDelimited_basic(self):
        output = self._run('print("hello world".toNonColonDelimited())')
        assert output[-1] == "hello:::::::::world"

    def test_toNonColonDelimited_three(self):
        output = self._run('print("a b c".toNonColonDelimited())')
        assert output[-1] == "a:::::::::b:::::::::c"
