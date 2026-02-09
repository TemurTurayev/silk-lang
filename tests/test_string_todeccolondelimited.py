"""
Tests for string .toDecColonDelimited() method - split words by :::::::::: (10 colons).
"""

from silk.interpreter import Interpreter


class TestStringToDecColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecColonDelimited_basic(self):
        output = self._run('print("hello world".toDecColonDelimited())')
        assert output[-1] == "hello::::::::::world"

    def test_toDecColonDelimited_three(self):
        output = self._run('print("a b c".toDecColonDelimited())')
        assert output[-1] == "a::::::::::b::::::::::c"
