"""
Tests for string .toSeptendecPipeDelimited() method - join words with 17 pipes.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecPipeDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecPipeDelimited())')
        assert output[-1] == "hello" + "|" * 17 + "world"

    def test_toSeptendecPipeDelimited_three(self):
        output = self._run('print("a b c".toSeptendecPipeDelimited())')
        assert output[-1] == "a" + "|" * 17 + "b" + "|" * 17 + "c"
