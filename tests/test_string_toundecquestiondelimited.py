"""
Tests for string .toUndecQuestionDelimited() method - split words by ??????????? (11 question marks).
"""

from silk.interpreter import Interpreter


class TestStringToUndecQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecQuestionDelimited_basic(self):
        output = self._run('print("hello world".toUndecQuestionDelimited())')
        assert output[-1] == "hello???????????world"

    def test_toUndecQuestionDelimited_three(self):
        output = self._run('print("a b c".toUndecQuestionDelimited())')
        assert output[-1] == "a???????????b???????????c"
