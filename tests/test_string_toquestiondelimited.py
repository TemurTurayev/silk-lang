"""
Tests for string .toQuestionDelimited() method - split words by question mark.
"""

from silk.interpreter import Interpreter


class TestStringToQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuestionDelimited_basic(self):
        output = self._run('print("hello world".toQuestionDelimited())')
        assert output[-1] == "hello?world"

    def test_toQuestionDelimited_three(self):
        output = self._run('print("a b c".toQuestionDelimited())')
        assert output[-1] == "a?b?c"
