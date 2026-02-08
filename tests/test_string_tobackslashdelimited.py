"""
Tests for string .toBackslashDelimited() method - split words by backslash.
"""

from silk.interpreter import Interpreter


class TestStringToBackslashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBackslashDelimited_basic(self):
        output = self._run('print("hello world".toBackslashDelimited())')
        assert output[-1] == "hello\\world"

    def test_toBackslashDelimited_three(self):
        output = self._run('print("a b c".toBackslashDelimited())')
        assert output[-1] == "a\\b\\c"
