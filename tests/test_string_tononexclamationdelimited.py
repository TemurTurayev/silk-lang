"""
Tests for string .toNonExclamationDelimited() method - split words by !!!!!!!!! (9 exclamations).
"""

from silk.interpreter import Interpreter


class TestStringToNonExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonExclamationDelimited_basic(self):
        output = self._run('print("hello world".toNonExclamationDelimited())')
        assert output[-1] == "hello!!!!!!!!!world"

    def test_toNonExclamationDelimited_three(self):
        output = self._run('print("a b c".toNonExclamationDelimited())')
        assert output[-1] == "a!!!!!!!!!b!!!!!!!!!c"
