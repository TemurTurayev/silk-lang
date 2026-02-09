"""
Tests for string .toVigintiQuestionDelimited() method - join words with 20 question marks.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiQuestionDelimited_basic(self):
        output = self._run('print("hello world".toVigintiQuestionDelimited())')
        assert output[-1] == "hello" + "?" * 20 + "world"

    def test_toVigintiQuestionDelimited_multi(self):
        output = self._run('print("a b c".toVigintiQuestionDelimited())')
        assert output[-1] == "a" + "?" * 20 + "b" + "?" * 20 + "c"
