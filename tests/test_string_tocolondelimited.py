"""
Tests for string .toColonDelimited() method - split words by colon.
"""

from silk.interpreter import Interpreter


class TestStringToColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toColonDelimited_basic(self):
        output = self._run('print("hello world".toColonDelimited())')
        assert output[-1] == "hello:world"

    def test_toColonDelimited_three(self):
        output = self._run('print("a b c".toColonDelimited())')
        assert output[-1] == "a:b:c"
