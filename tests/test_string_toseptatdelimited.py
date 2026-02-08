"""
Tests for string .toSeptAtDelimited() method - split words by @@@@@@@.
"""

from silk.interpreter import Interpreter


class TestStringToSeptAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptAtDelimited_basic(self):
        output = self._run('print("hello world".toSeptAtDelimited())')
        assert output[-1] == "hello@@@@@@@world"

    def test_toSeptAtDelimited_three(self):
        output = self._run('print("a b c".toSeptAtDelimited())')
        assert output[-1] == "a@@@@@@@b@@@@@@@c"
