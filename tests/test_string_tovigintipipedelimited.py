"""
Tests for string .toVigintiPipeDelimited() method - join words with 20 pipes.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiPipeDelimited_basic(self):
        output = self._run('print("hello world".toVigintiPipeDelimited())')
        assert output[-1] == "hello||||||||||||||||||||world"

    def test_toVigintiPipeDelimited_multi(self):
        output = self._run('print("a b c".toVigintiPipeDelimited())')
        assert output[-1] == "a||||||||||||||||||||b||||||||||||||||||||c"
