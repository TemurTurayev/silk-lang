"""
Tests for string .toQuindecQuestionDelimited() method - join words with 15 question marks.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecQuestionDelimited_basic(self):
        output = self._run('print("hello world".toQuindecQuestionDelimited())')
        assert output[-1] == "hello???????????????world"

    def test_toQuindecQuestionDelimited_three(self):
        output = self._run('print("a b c".toQuindecQuestionDelimited())')
        assert output[-1] == "a???????????????b???????????????c"
