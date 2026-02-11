"""
Tests for string .toUnvigintiQuestionDelimited() method - join words with 21 question marks.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiQuestionDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiQuestionDelimited())')
        assert output[-1] == "hello" + "?" * 21 + "world"

    def test_toUnvigintiQuestionDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiQuestionDelimited())')
        assert output[-1] == "a" + "?" * 21 + "b" + "?" * 21 + "c"
