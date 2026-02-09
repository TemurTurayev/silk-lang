"""
Tests for string .toVigintiDotDelimited() method - join words with 20 dots.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiDotDelimited_basic(self):
        output = self._run('print("hello world".toVigintiDotDelimited())')
        assert output[-1] == "hello....................world"

    def test_toVigintiDotDelimited_multi(self):
        output = self._run('print("a b c".toVigintiDotDelimited())')
        assert output[-1] == "a....................b....................c"
