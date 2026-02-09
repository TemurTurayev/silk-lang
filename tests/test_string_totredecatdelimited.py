"""
Tests for string .toTredecAtDelimited() method - join words with 13 at signs.
"""

from silk.interpreter import Interpreter


class TestStringToTredecAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecAtDelimited_basic(self):
        output = self._run('print("hello world".toTredecAtDelimited())')
        assert output[-1] == "hello@@@@@@@@@@@@@world"

    def test_toTredecAtDelimited_three(self):
        output = self._run('print("a b c".toTredecAtDelimited())')
        assert output[-1] == "a@@@@@@@@@@@@@b@@@@@@@@@@@@@c"
