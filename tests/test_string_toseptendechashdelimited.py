"""
Tests for string .toSeptendecHashDelimited() method - join words with 17 hashes.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecHashDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecHashDelimited())')
        assert output[-1] == "hello" + "#" * 17 + "world"

    def test_toSeptendecHashDelimited_three(self):
        output = self._run('print("a b c".toSeptendecHashDelimited())')
        assert output[-1] == "a" + "#" * 17 + "b" + "#" * 17 + "c"
