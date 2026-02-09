"""
Tests for string .toQuattuordecPipeDelimited() method - join words with 14 pipes.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecPipeDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecPipeDelimited())')
        assert output[-1] == "hello||||||||||||||world"

    def test_toQuattuordecPipeDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecPipeDelimited())')
        assert output[-1] == "a||||||||||||||b||||||||||||||c"
