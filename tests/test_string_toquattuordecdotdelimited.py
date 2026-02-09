"""
Tests for string .toQuattuordecDotDelimited() method - join words with 14 dots.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecDotDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecDotDelimited())')
        assert output[-1] == "hello..............world"

    def test_toQuattuordecDotDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecDotDelimited())')
        assert output[-1] == "a..............b..............c"
