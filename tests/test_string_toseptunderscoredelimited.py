"""
Tests for string .toSeptUnderscoreDelimited() method - split words by _______.
"""

from silk.interpreter import Interpreter


class TestStringToSeptUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toSeptUnderscoreDelimited())')
        assert output[-1] == "hello_______world"

    def test_toSeptUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toSeptUnderscoreDelimited())')
        assert output[-1] == "a_______b_______c"
