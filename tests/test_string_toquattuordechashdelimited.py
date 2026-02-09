"""
Tests for string .toQuattuordecHashDelimited() method - join words with 14 hashes.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecHashDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecHashDelimited())')
        assert output[-1] == "hello##############world"

    def test_toQuattuordecHashDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecHashDelimited())')
        assert output[-1] == "a##############b##############c"
