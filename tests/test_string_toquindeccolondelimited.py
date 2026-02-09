"""
Tests for string .toQuindecColonDelimited() method - join words with 15 colons.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecColonDelimited_basic(self):
        output = self._run('print("hello world".toQuindecColonDelimited())')
        assert output[-1] == "hello:::::::::::::::world"

    def test_toQuindecColonDelimited_three(self):
        output = self._run('print("a b c".toQuindecColonDelimited())')
        assert output[-1] == "a:::::::::::::::b:::::::::::::::c"
