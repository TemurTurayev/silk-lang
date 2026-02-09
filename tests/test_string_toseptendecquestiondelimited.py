"""
Tests for string .toSeptendecQuestionDelimited() method - join words with 17 question marks.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecQuestionDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecQuestionDelimited())')
        assert output[-1] == "hello" + "?" * 17 + "world"

    def test_toSeptendecQuestionDelimited_three(self):
        output = self._run('print("a b c".toSeptendecQuestionDelimited())')
        assert output[-1] == "a" + "?" * 17 + "b" + "?" * 17 + "c"
