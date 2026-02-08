"""
Tests for string .toSextQuestionDelimited() method - split words by ??????.
"""

from silk.interpreter import Interpreter


class TestStringToSextQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextQuestionDelimited_basic(self):
        output = self._run('print("hello world".toSextQuestionDelimited())')
        assert output[-1] == "hello??????world"

    def test_toSextQuestionDelimited_three(self):
        output = self._run('print("a b c".toSextQuestionDelimited())')
        assert output[-1] == "a??????b??????c"
