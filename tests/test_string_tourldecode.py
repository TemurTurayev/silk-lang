"""
Tests for string .toURLDecode() method - URL-decode the string.
"""

from silk.interpreter import Interpreter


class TestStringToURLDecode:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toURLDecode_space(self):
        output = self._run('print("hello%20world".toURLDecode())')
        assert output[-1] == "hello world"

    def test_toURLDecode_special(self):
        output = self._run('print("a%26b%3Dc".toURLDecode())')
        assert output[-1] == "a&b=c"
