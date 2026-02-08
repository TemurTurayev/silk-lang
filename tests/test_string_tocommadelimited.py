"""
Tests for string .toCommaDelimited() method - split words by comma.
"""

from silk.interpreter import Interpreter


class TestStringToCommaDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCommaDelimited_basic(self):
        output = self._run('print("hello world".toCommaDelimited())')
        assert output[-1] == "hello,world"

    def test_toCommaDelimited_three(self):
        output = self._run('print("a b c".toCommaDelimited())')
        assert output[-1] == "a,b,c"
