"""
Tests for string .toQuattuordecQuestionDelimited() method - join words with 14 question marks.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecQuestionDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecQuestionDelimited())')
        assert output[-1] == "hello??????????????world"

    def test_toQuattuordecQuestionDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecQuestionDelimited())')
        assert output[-1] == "a??????????????b??????????????c"
