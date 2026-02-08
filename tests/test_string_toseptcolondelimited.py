"""
Tests for string .toSeptColonDelimited() method - split words by :::::::.
"""

from silk.interpreter import Interpreter


class TestStringToSeptColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptColonDelimited_basic(self):
        output = self._run('print("hello world".toSeptColonDelimited())')
        assert output[-1] == "hello:::::::world"

    def test_toSeptColonDelimited_three(self):
        output = self._run('print("a b c".toSeptColonDelimited())')
        assert output[-1] == "a:::::::b:::::::c"
