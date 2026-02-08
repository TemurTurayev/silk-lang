"""
Tests for string .toOctQuestionDelimited() method - split words by ????????.
"""

from silk.interpreter import Interpreter


class TestStringToOctQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctQuestionDelimited_basic(self):
        output = self._run('print("hello world".toOctQuestionDelimited())')
        assert output[-1] == "hello????????world"

    def test_toOctQuestionDelimited_three(self):
        output = self._run('print("a b c".toOctQuestionDelimited())')
        assert output[-1] == "a????????b????????c"
