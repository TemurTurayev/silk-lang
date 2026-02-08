"""
Tests for string .toDecAtDelimited() method - split words by @@@@@@@@@@ (10 ats).
"""

from silk.interpreter import Interpreter


class TestStringToDecAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecAtDelimited_basic(self):
        output = self._run('print("hello world".toDecAtDelimited())')
        assert output[-1] == "hello@@@@@@@@@@world"

    def test_toDecAtDelimited_three(self):
        output = self._run('print("a b c".toDecAtDelimited())')
        assert output[-1] == "a@@@@@@@@@@b@@@@@@@@@@c"
