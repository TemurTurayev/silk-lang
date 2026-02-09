"""
Tests for string .toOctodecHashDelimited() method - join words with 18 hashes.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecHashDelimited_basic(self):
        output = self._run('print("hello world".toOctodecHashDelimited())')
        assert output[-1] == "hello" + "#" * 18 + "world"

    def test_toOctodecHashDelimited_three(self):
        output = self._run('print("a b c".toOctodecHashDelimited())')
        assert output[-1] == "a" + "#" * 18 + "b" + "#" * 18 + "c"
