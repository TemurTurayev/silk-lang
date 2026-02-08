"""
Tests for string .toQuintAtDelimited() method - split words by @@@@@.
"""

from silk.interpreter import Interpreter


class TestStringToQuintAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintAtDelimited_basic(self):
        output = self._run('print("hello world".toQuintAtDelimited())')
        assert output[-1] == "hello@@@@@world"

    def test_toQuintAtDelimited_three(self):
        output = self._run('print("a b c".toQuintAtDelimited())')
        assert output[-1] == "a@@@@@b@@@@@c"
