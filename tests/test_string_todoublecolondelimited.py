"""
Tests for string .toDoubleColonDelimited() method - split words by ::.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleColonDelimited_basic(self):
        output = self._run('print("hello world".toDoubleColonDelimited())')
        assert output[-1] == "hello::world"

    def test_toDoubleColonDelimited_three(self):
        output = self._run('print("a b c".toDoubleColonDelimited())')
        assert output[-1] == "a::b::c"
