"""
Tests for string .toSextAtDelimited() method - split words by @@@@@@.
"""

from silk.interpreter import Interpreter


class TestStringToSextAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextAtDelimited_basic(self):
        output = self._run('print("hello world".toSextAtDelimited())')
        assert output[-1] == "hello@@@@@@world"

    def test_toSextAtDelimited_three(self):
        output = self._run('print("a b c".toSextAtDelimited())')
        assert output[-1] == "a@@@@@@b@@@@@@c"
