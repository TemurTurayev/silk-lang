"""
Tests for string .toUndecAtDelimited() method - split words by @@@@@@@@@@@ (11 at signs).
"""

from silk.interpreter import Interpreter


class TestStringToUndecAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecAtDelimited_basic(self):
        output = self._run('print("hello world".toUndecAtDelimited())')
        assert output[-1] == "hello@@@@@@@@@@@world"

    def test_toUndecAtDelimited_three(self):
        output = self._run('print("a b c".toUndecAtDelimited())')
        assert output[-1] == "a@@@@@@@@@@@b@@@@@@@@@@@c"
