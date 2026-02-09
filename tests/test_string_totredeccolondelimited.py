"""
Tests for string .toTredecColonDelimited() method - join words with 13 colons.
"""

from silk.interpreter import Interpreter


class TestStringToTredecColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecColonDelimited_basic(self):
        output = self._run('print("hello world".toTredecColonDelimited())')
        assert output[-1] == "hello:::::::::::::world"

    def test_toTredecColonDelimited_three(self):
        output = self._run('print("a b c".toTredecColonDelimited())')
        assert output[-1] == "a:::::::::::::b:::::::::::::c"
