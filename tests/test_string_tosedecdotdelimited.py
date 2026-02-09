"""
Tests for string .toSedecDotDelimited() method - join words with 16 dots.
"""

from silk.interpreter import Interpreter


class TestStringToSedecDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecDotDelimited_basic(self):
        output = self._run('print("hello world".toSedecDotDelimited())')
        assert output[-1] == "hello................world"

    def test_toSedecDotDelimited_three(self):
        output = self._run('print("a b c".toSedecDotDelimited())')
        assert output[-1] == "a................b................c"
