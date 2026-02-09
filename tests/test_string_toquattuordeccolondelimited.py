"""
Tests for string .toQuattuordecColonDelimited() method - join words with 14 colons.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecColonDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecColonDelimited())')
        assert output[-1] == "hello::::::::::::::world"

    def test_toQuattuordecColonDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecColonDelimited())')
        assert output[-1] == "a::::::::::::::b::::::::::::::c"
