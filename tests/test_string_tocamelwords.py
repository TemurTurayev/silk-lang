"""
Tests for string .toCamelWords() method - split camelCase into words.
"""

from silk.interpreter import Interpreter


class TestStringToCamelWords:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCamelWords_basic(self):
        output = self._run('print("myVarName".toCamelWords())')
        assert output[-1] == "[my, Var, Name]"

    def test_toCamelWords_simple(self):
        output = self._run('print("hello".toCamelWords())')
        assert output[-1] == "[hello]"
