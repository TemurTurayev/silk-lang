"""
Tests for string .toSeptendecExclamationDelimited() method - join words with 17 exclamation marks.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecExclamationDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecExclamationDelimited())')
        assert output[-1] == "hello" + "!" * 17 + "world"

    def test_toSeptendecExclamationDelimited_three(self):
        output = self._run('print("a b c".toSeptendecExclamationDelimited())')
        assert output[-1] == "a" + "!" * 17 + "b" + "!" * 17 + "c"
