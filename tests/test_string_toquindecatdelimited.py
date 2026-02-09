"""
Tests for string .toQuindecAtDelimited() method - join words with 15 at signs.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecAtDelimited_basic(self):
        output = self._run('print("hello world".toQuindecAtDelimited())')
        assert output[-1] == "hello@@@@@@@@@@@@@@@world"

    def test_toQuindecAtDelimited_three(self):
        output = self._run('print("a b c".toQuindecAtDelimited())')
        assert output[-1] == "a@@@@@@@@@@@@@@@b@@@@@@@@@@@@@@@c"
