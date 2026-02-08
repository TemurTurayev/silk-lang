"""
Tests for string .toCurlyBraced() method - wrap string in curly braces.
"""

from silk.interpreter import Interpreter


class TestStringToCurlyBraced:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCurlyBraced_basic(self):
        output = self._run('print("hello".toCurlyBraced())')
        assert output[-1] == "{hello}"

    def test_toCurlyBraced_word(self):
        output = self._run('print("test".toCurlyBraced())')
        assert output[-1] == "{test}"
