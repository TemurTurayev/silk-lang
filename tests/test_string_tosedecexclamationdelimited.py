"""
Tests for string .toSedecExclamationDelimited() method - join words with 16 exclamation marks.
"""

from silk.interpreter import Interpreter


class TestStringToSedecExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecExclamationDelimited_basic(self):
        output = self._run('print("hello world".toSedecExclamationDelimited())')
        assert output[-1] == "hello" + "!" * 16 + "world"

    def test_toSedecExclamationDelimited_three(self):
        output = self._run('print("a b c".toSedecExclamationDelimited())')
        assert output[-1] == "a" + "!" * 16 + "b" + "!" * 16 + "c"
