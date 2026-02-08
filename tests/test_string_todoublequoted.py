"""
Tests for string .toDoubleQuoted() method - wrap string in double quotes.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleQuoted:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleQuoted_basic(self):
        output = self._run('print("hello".toDoubleQuoted())')
        assert output[-1] == '"hello"'

    def test_toDoubleQuoted_word(self):
        output = self._run('print("world".toDoubleQuoted())')
        assert output[-1] == '"world"'
