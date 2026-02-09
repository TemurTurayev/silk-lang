"""
Tests for string .toSedecPipeDelimited() method - join words with 16 pipes.
"""

from silk.interpreter import Interpreter


class TestStringToSedecPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecPipeDelimited_basic(self):
        output = self._run('print("hello world".toSedecPipeDelimited())')
        assert output[-1] == "hello||||||||||||||||world"

    def test_toSedecPipeDelimited_three(self):
        output = self._run('print("a b c".toSedecPipeDelimited())')
        assert output[-1] == "a||||||||||||||||b||||||||||||||||c"
