"""
Tests for string .toSextDotDelimited() method - split words by ......
"""

from silk.interpreter import Interpreter


class TestStringToSextDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextDotDelimited_basic(self):
        output = self._run('print("hello world".toSextDotDelimited())')
        assert output[-1] == "hello......world"

    def test_toSextDotDelimited_three(self):
        output = self._run('print("a b c".toSextDotDelimited())')
        assert output[-1] == "a......b......c"
