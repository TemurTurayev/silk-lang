"""
Tests for string .toOctColonDelimited() method - split words by ::::::::.
"""

from silk.interpreter import Interpreter


class TestStringToOctColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctColonDelimited_basic(self):
        output = self._run('print("hello world".toOctColonDelimited())')
        assert output[-1] == "hello::::::::world"

    def test_toOctColonDelimited_three(self):
        output = self._run('print("a b c".toOctColonDelimited())')
        assert output[-1] == "a::::::::b::::::::c"
