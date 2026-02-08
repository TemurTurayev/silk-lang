"""
Tests for string .toSextExclamationDelimited() method - split words by !!!!!!.
"""

from silk.interpreter import Interpreter


class TestStringToSextExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextExclamationDelimited_basic(self):
        output = self._run('print("hello world".toSextExclamationDelimited())')
        assert output[-1] == "hello!!!!!!world"

    def test_toSextExclamationDelimited_three(self):
        output = self._run('print("a b c".toSextExclamationDelimited())')
        assert output[-1] == "a!!!!!!b!!!!!!c"
