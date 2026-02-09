"""
Tests for string .toQuattuordecAtDelimited() method - join words with 14 at signs.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecAtDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecAtDelimited())')
        assert output[-1] == "hello@@@@@@@@@@@@@@world"

    def test_toQuattuordecAtDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecAtDelimited())')
        assert output[-1] == "a@@@@@@@@@@@@@@b@@@@@@@@@@@@@@c"
