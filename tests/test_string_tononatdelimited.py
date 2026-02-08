"""
Tests for string .toNonAtDelimited() method - split words by @@@@@@@@@ (9 ats).
"""

from silk.interpreter import Interpreter


class TestStringToNonAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonAtDelimited_basic(self):
        output = self._run('print("hello world".toNonAtDelimited())')
        assert output[-1] == "hello@@@@@@@@@world"

    def test_toNonAtDelimited_three(self):
        output = self._run('print("a b c".toNonAtDelimited())')
        assert output[-1] == "a@@@@@@@@@b@@@@@@@@@c"
