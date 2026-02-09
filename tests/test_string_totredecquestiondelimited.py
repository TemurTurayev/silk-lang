"""
Tests for string .toTredecQuestionDelimited() method - join words with 13 question marks.
"""

from silk.interpreter import Interpreter


class TestStringToTredecQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecQuestionDelimited_basic(self):
        output = self._run('print("hello world".toTredecQuestionDelimited())')
        assert output[-1] == "hello?????????????world"

    def test_toTredecQuestionDelimited_three(self):
        output = self._run('print("a b c".toTredecQuestionDelimited())')
        assert output[-1] == "a?????????????b?????????????c"
