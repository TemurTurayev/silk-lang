"""
Tests for string .toTripleDashDelimited() method - split words by ---.
"""

from silk.interpreter import Interpreter


class TestStringToTripleDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleDashDelimited_basic(self):
        output = self._run('print("hello world".toTripleDashDelimited())')
        assert output[-1] == "hello---world"

    def test_toTripleDashDelimited_three(self):
        output = self._run('print("a b c".toTripleDashDelimited())')
        assert output[-1] == "a---b---c"
