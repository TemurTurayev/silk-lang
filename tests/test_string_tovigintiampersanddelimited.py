"""
Tests for string .toVigintiAmpersandDelimited() method - join words with 20 ampersands.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toVigintiAmpersandDelimited())')
        assert output[-1] == "hello" + "&" * 20 + "world"

    def test_toVigintiAmpersandDelimited_multi(self):
        output = self._run('print("a b c".toVigintiAmpersandDelimited())')
        assert output[-1] == "a" + "&" * 20 + "b" + "&" * 20 + "c"
