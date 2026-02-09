"""
Tests for string .toQuattuordecExclamationDelimited() method - join words with 14 exclamation marks.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecExclamationDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecExclamationDelimited())')
        assert output[-1] == "hello!!!!!!!!!!!!!!world"

    def test_toQuattuordecExclamationDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecExclamationDelimited())')
        assert output[-1] == "a!!!!!!!!!!!!!!b!!!!!!!!!!!!!!c"
