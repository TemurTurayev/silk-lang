"""
Tests for string .toCharArray() method - split into individual characters.
"""

from silk.interpreter import Interpreter


class TestStringToCharArray:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCharArray_basic(self):
        output = self._run('print("hi".toCharArray())')
        assert output[-1] == "[h, i]"

    def test_toCharArray_longer(self):
        output = self._run('print("abc".toCharArray())')
        assert output[-1] == "[a, b, c]"
