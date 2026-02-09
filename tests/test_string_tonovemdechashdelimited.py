"""
Tests for string .toNovemdecHashDelimited() method - join words with 19 hashes.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecHashDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecHashDelimited())')
        assert output[-1] == "hello" + "#" * 19 + "world"

    def test_toNovemdecHashDelimited_three(self):
        output = self._run('print("a b c".toNovemdecHashDelimited())')
        assert output[-1] == "a" + "#" * 19 + "b" + "#" * 19 + "c"
