"""
Tests for string .toSedecQuestionDelimited() method - join words with 16 question marks.
"""

from silk.interpreter import Interpreter


class TestStringToSedecQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecQuestionDelimited_basic(self):
        output = self._run('print("hello world".toSedecQuestionDelimited())')
        assert output[-1] == "hello" + "?" * 16 + "world"

    def test_toSedecQuestionDelimited_three(self):
        output = self._run('print("a b c".toSedecQuestionDelimited())')
        assert output[-1] == "a" + "?" * 16 + "b" + "?" * 16 + "c"
