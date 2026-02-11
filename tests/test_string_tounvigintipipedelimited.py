"""
Tests for string .toUnvigintiPipeDelimited() method - join words with 21 pipes.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiPipeDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiPipeDelimited())')
        assert output[-1] == "hello" + "|" * 21 + "world"

    def test_toUnvigintiPipeDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiPipeDelimited())')
        assert output[-1] == "a" + "|" * 21 + "b" + "|" * 21 + "c"
