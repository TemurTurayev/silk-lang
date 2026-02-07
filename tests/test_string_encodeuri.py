"""
Tests for string .encodeURI() method.
"""

from silk.interpreter import Interpreter


class TestStringEncodeURI:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_encodeURI_space(self):
        output = self._run('print("hello world".encodeURI())')
        assert output[-1] == "hello%20world"

    def test_encodeURI_special(self):
        output = self._run('print("a&b=c".encodeURI())')
        assert output[-1] == "a%26b%3Dc"
