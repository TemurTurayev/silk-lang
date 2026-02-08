"""
Tests for string .toDecQuestionDelimited() method - split words by ?????????? (10 question marks).
"""

from silk.interpreter import Interpreter


class TestStringToDecQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecQuestionDelimited_basic(self):
        output = self._run('print("hello world".toDecQuestionDelimited())')
        assert output[-1] == "hello??????????world"

    def test_toDecQuestionDelimited_three(self):
        output = self._run('print("a b c".toDecQuestionDelimited())')
        assert output[-1] == "a??????????b??????????c"
