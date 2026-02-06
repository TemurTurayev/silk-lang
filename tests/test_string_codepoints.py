"""
Tests for string .codePoints() method.
"""

from silk.interpreter import Interpreter


class TestStringCodePoints:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_codePoints_ascii(self):
        output = self._run('print("ABC".codePoints())')
        assert output[-1] == "[65, 66, 67]"

    def test_codePoints_hello(self):
        output = self._run('print("hi".codePoints())')
        assert output[-1] == "[104, 105]"

    def test_codePoints_empty(self):
        output = self._run('print("".codePoints())')
        assert output[-1] == "[]"
