"""
Tests for string .toURLEncode() method - URL-encode the string.
"""

from silk.interpreter import Interpreter


class TestStringToURLEncode:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toURLEncode_space(self):
        output = self._run('print("hello world".toURLEncode())')
        assert output[-1] == "hello%20world"

    def test_toURLEncode_special(self):
        output = self._run('print("a&b=c".toURLEncode())')
        assert output[-1] == "a%26b%3Dc"
