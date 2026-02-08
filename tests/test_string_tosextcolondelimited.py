"""
Tests for string .toSextColonDelimited() method - split words by ::::::.
"""

from silk.interpreter import Interpreter


class TestStringToSextColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextColonDelimited_basic(self):
        output = self._run('print("hello world".toSextColonDelimited())')
        assert output[-1] == "hello::::::world"

    def test_toSextColonDelimited_three(self):
        output = self._run('print("a b c".toSextColonDelimited())')
        assert output[-1] == "a::::::b::::::c"
