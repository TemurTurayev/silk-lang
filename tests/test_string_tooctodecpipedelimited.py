"""
Tests for string .toOctodecPipeDelimited() method - join words with 18 pipes.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecPipeDelimited_basic(self):
        output = self._run('print("hello world".toOctodecPipeDelimited())')
        assert output[-1] == "hello" + "|" * 18 + "world"

    def test_toOctodecPipeDelimited_three(self):
        output = self._run('print("a b c".toOctodecPipeDelimited())')
        assert output[-1] == "a" + "|" * 18 + "b" + "|" * 18 + "c"
