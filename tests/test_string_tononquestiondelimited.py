"""
Tests for string .toNonQuestionDelimited() method - split words by ????????? (9 question marks).
"""

from silk.interpreter import Interpreter


class TestStringToNonQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonQuestionDelimited_basic(self):
        output = self._run('print("hello world".toNonQuestionDelimited())')
        assert output[-1] == "hello?????????world"

    def test_toNonQuestionDelimited_three(self):
        output = self._run('print("a b c".toNonQuestionDelimited())')
        assert output[-1] == "a?????????b?????????c"
