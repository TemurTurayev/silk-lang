"""
Tests for string .decodeURI() method.
"""

from silk.interpreter import Interpreter


class TestStringDecodeURI:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_decodeURI_space(self):
        output = self._run('print("hello%20world".decodeURI())')
        assert output[-1] == "hello world"

    def test_decodeURI_special(self):
        output = self._run('print("a%26b%3Dc".decodeURI())')
        assert output[-1] == "a&b=c"
