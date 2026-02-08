"""
Tests for string .toQuadQuestionDelimited() method - split words by ????.
"""

from silk.interpreter import Interpreter


class TestStringToQuadQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadQuestionDelimited_basic(self):
        output = self._run('print("hello world".toQuadQuestionDelimited())')
        assert output[-1] == "hello????world"

    def test_toQuadQuestionDelimited_three(self):
        output = self._run('print("a b c".toQuadQuestionDelimited())')
        assert output[-1] == "a????b????c"
