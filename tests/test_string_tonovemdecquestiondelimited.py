"""
Tests for string .toNovemdecQuestionDelimited() method - join words with 19 question marks.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecQuestionDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecQuestionDelimited())')
        assert output[-1] == "hello" + "?" * 19 + "world"

    def test_toNovemdecQuestionDelimited_three(self):
        output = self._run('print("a b c".toNovemdecQuestionDelimited())')
        assert output[-1] == "a" + "?" * 19 + "b" + "?" * 19 + "c"
