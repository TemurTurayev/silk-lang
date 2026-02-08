"""
Tests for string .toSingleQuoted() method - wrap string in single quotes.
"""

from silk.interpreter import Interpreter


class TestStringToSingleQuoted:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSingleQuoted_basic(self):
        output = self._run('print("hello".toSingleQuoted())')
        assert output[-1] == "'hello'"

    def test_toSingleQuoted_word(self):
        output = self._run('print("world".toSingleQuoted())')
        assert output[-1] == "'world'"
