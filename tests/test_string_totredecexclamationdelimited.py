"""
Tests for string .toTredecExclamationDelimited() method - join words with 13 exclamation marks.
"""

from silk.interpreter import Interpreter


class TestStringToTredecExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecExclamationDelimited_basic(self):
        output = self._run('print("hello world".toTredecExclamationDelimited())')
        assert output[-1] == "hello!!!!!!!!!!!!!world"

    def test_toTredecExclamationDelimited_three(self):
        output = self._run('print("a b c".toTredecExclamationDelimited())')
        assert output[-1] == "a!!!!!!!!!!!!!b!!!!!!!!!!!!!c"
