"""
Tests for string .toNovemdecPipeDelimited() method - join words with 19 pipes.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecPipeDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecPipeDelimited())')
        assert output[-1] == "hello" + "|" * 19 + "world"

    def test_toNovemdecPipeDelimited_three(self):
        output = self._run('print("a b c".toNovemdecPipeDelimited())')
        assert output[-1] == "a" + "|" * 19 + "b" + "|" * 19 + "c"
