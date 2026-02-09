"""
Tests for string .toDuodecQuestionDelimited() method - split words by ???????????? (12 questions).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecQuestionDelimited_basic(self):
        output = self._run('print("hello world".toDuodecQuestionDelimited())')
        assert output[-1] == "hello????????????world"

    def test_toDuodecQuestionDelimited_three(self):
        output = self._run('print("a b c".toDuodecQuestionDelimited())')
        assert output[-1] == "a????????????b????????????c"
