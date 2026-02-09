"""
Tests for string .toQuindecExclamationDelimited() method - join words with 15 exclamation marks.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecExclamationDelimited_basic(self):
        output = self._run('print("hello world".toQuindecExclamationDelimited())')
        assert output[-1] == "hello!!!!!!!!!!!!!!!world"

    def test_toQuindecExclamationDelimited_three(self):
        output = self._run('print("a b c".toQuindecExclamationDelimited())')
        assert output[-1] == "a!!!!!!!!!!!!!!!b!!!!!!!!!!!!!!!c"
