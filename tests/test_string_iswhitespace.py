"""
Tests for string .isWhitespace() method.
"""

from silk.interpreter import Interpreter


class TestStringIsWhitespace:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isWhitespace_true(self):
        output = self._run('print("   ".isWhitespace())')
        assert output[-1] == "true"

    def test_isWhitespace_false(self):
        output = self._run('print("hello".isWhitespace())')
        assert output[-1] == "false"

    def test_isWhitespace_empty(self):
        output = self._run('print("".isWhitespace())')
        assert output[-1] == "false"
