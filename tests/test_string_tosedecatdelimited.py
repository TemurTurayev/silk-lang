"""
Tests for string .toSedecAtDelimited() method - join words with 16 at signs.
"""

from silk.interpreter import Interpreter


class TestStringToSedecAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecAtDelimited_basic(self):
        output = self._run('print("hello world".toSedecAtDelimited())')
        assert output[-1] == "hello@@@@@@@@@@@@@@@@world"

    def test_toSedecAtDelimited_three(self):
        output = self._run('print("a b c".toSedecAtDelimited())')
        assert output[-1] == "a@@@@@@@@@@@@@@@@b@@@@@@@@@@@@@@@@c"
