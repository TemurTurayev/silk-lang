"""
Tests for string .trimLines() method.
"""

from silk.interpreter import Interpreter


class TestStringTrimLines:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_trimLines_basic(self):
        output = self._run(r'print("  hello  \n  world  ".trimLines())')
        assert output[-1] == "hello\nworld"

    def test_trimLines_mixed(self):
        output = self._run(r'print("foo\n  bar  \nbaz".trimLines())')
        assert output[-1] == "foo\nbar\nbaz"
