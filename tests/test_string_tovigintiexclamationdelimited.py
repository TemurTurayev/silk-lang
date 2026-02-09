"""
Tests for string .toVigintiExclamationDelimited() method - join words with 20 exclamation marks.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiExclamationDelimited_basic(self):
        output = self._run('print("hello world".toVigintiExclamationDelimited())')
        assert output[-1] == "hello" + "!" * 20 + "world"

    def test_toVigintiExclamationDelimited_multi(self):
        output = self._run('print("a b c".toVigintiExclamationDelimited())')
        assert output[-1] == "a" + "!" * 20 + "b" + "!" * 20 + "c"
