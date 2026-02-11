"""
Tests for string .toUnvigintiExclamationDelimited() method - join words with 21 exclamation marks.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiExclamationDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiExclamationDelimited())')
        assert output[-1] == "hello" + "!" * 21 + "world"

    def test_toUnvigintiExclamationDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiExclamationDelimited())')
        assert output[-1] == "a" + "!" * 21 + "b" + "!" * 21 + "c"
