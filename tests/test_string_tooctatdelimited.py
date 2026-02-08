"""
Tests for string .toOctAtDelimited() method - split words by @@@@@@@@.
"""

from silk.interpreter import Interpreter


class TestStringToOctAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctAtDelimited_basic(self):
        output = self._run('print("hello world".toOctAtDelimited())')
        assert output[-1] == "hello@@@@@@@@world"

    def test_toOctAtDelimited_three(self):
        output = self._run('print("a b c".toOctAtDelimited())')
        assert output[-1] == "a@@@@@@@@b@@@@@@@@c"
