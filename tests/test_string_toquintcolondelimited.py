"""
Tests for string .toQuintColonDelimited() method - split words by :::::.
"""

from silk.interpreter import Interpreter


class TestStringToQuintColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintColonDelimited_basic(self):
        output = self._run('print("hello world".toQuintColonDelimited())')
        assert output[-1] == "hello:::::world"

    def test_toQuintColonDelimited_three(self):
        output = self._run('print("a b c".toQuintColonDelimited())')
        assert output[-1] == "a:::::b:::::c"
