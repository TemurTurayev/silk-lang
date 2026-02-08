"""
Tests for string .toSeptDotDelimited() method - split words by .......
"""

from silk.interpreter import Interpreter


class TestStringToSeptDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptDotDelimited_basic(self):
        output = self._run('print("hello world".toSeptDotDelimited())')
        assert output[-1] == "hello.......world"

    def test_toSeptDotDelimited_three(self):
        output = self._run('print("a b c".toSeptDotDelimited())')
        assert output[-1] == "a.......b.......c"
