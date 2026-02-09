"""
Tests for string .toQuindecPipeDelimited() method - join words with 15 pipes.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecPipeDelimited_basic(self):
        output = self._run('print("hello world".toQuindecPipeDelimited())')
        assert output[-1] == "hello|||||||||||||||world"

    def test_toQuindecPipeDelimited_three(self):
        output = self._run('print("a b c".toQuindecPipeDelimited())')
        assert output[-1] == "a|||||||||||||||b|||||||||||||||c"
