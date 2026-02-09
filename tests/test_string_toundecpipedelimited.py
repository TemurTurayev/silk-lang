"""
Tests for string .toUndecPipeDelimited() method - split words by ||||||||||| (11 pipes).
"""

from silk.interpreter import Interpreter


class TestStringToUndecPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecPipeDelimited_basic(self):
        output = self._run('print("hello world".toUndecPipeDelimited())')
        assert output[-1] == "hello|||||||||||world"

    def test_toUndecPipeDelimited_three(self):
        output = self._run('print("a b c".toUndecPipeDelimited())')
        assert output[-1] == "a|||||||||||b|||||||||||c"
