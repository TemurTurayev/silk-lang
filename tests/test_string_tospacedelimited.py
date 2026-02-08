"""
Tests for string .toSpaceDelimited() method - join chars/words with spaces.
"""

from silk.interpreter import Interpreter


class TestStringToSpaceDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSpaceDelimited_basic(self):
        output = self._run('print("hello-world".toSpaceDelimited())')
        assert output[-1] == "hello world"

    def test_toSpaceDelimited_underscore(self):
        output = self._run('print("a_b_c".toSpaceDelimited())')
        assert output[-1] == "a b c"
