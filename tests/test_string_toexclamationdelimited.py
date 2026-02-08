"""
Tests for string .toExclamationDelimited() method - split words by exclamation mark.
"""

from silk.interpreter import Interpreter


class TestStringToExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toExclamationDelimited_basic(self):
        output = self._run('print("hello world".toExclamationDelimited())')
        assert output[-1] == "hello!world"

    def test_toExclamationDelimited_three(self):
        output = self._run('print("a b c".toExclamationDelimited())')
        assert output[-1] == "a!b!c"
