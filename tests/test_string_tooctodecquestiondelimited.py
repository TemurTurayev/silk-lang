"""
Tests for string .toOctodecQuestionDelimited() method - join words with 18 question marks.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecQuestionDelimited_basic(self):
        output = self._run('print("hello world".toOctodecQuestionDelimited())')
        assert output[-1] == "hello" + "?" * 18 + "world"

    def test_toOctodecQuestionDelimited_three(self):
        output = self._run('print("a b c".toOctodecQuestionDelimited())')
        assert output[-1] == "a" + "?" * 18 + "b" + "?" * 18 + "c"
