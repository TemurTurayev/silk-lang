"""
Tests for string .toWordArray() method - split into array of words.
"""

from silk.interpreter import Interpreter


class TestStringToWordArray:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toWordArray_basic(self):
        output = self._run('print("hello world".toWordArray())')
        assert output[-1] == "[hello, world]"

    def test_toWordArray_extra_spaces(self):
        output = self._run('print("  a  b  ".toWordArray())')
        assert output[-1] == "[a, b]"
