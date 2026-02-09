"""
Tests for string .toTredecPipeDelimited() method - join words with 13 pipes.
"""

from silk.interpreter import Interpreter


class TestStringToTredecPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecPipeDelimited_basic(self):
        output = self._run('print("hello world".toTredecPipeDelimited())')
        assert output[-1] == "hello|||||||||||||world"

    def test_toTredecPipeDelimited_three(self):
        output = self._run('print("a b c".toTredecPipeDelimited())')
        assert output[-1] == "a|||||||||||||b|||||||||||||c"
