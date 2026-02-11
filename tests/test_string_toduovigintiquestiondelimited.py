"""
Tests for string .toDuovigintiQuestionDelimited() method - join words with 22 question marks.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiQuestionDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiQuestionDelimited())')
        assert output[-1] == "hello" + "?" * 22 + "world"

    def test_toDuovigintiQuestionDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiQuestionDelimited())')
        assert output[-1] == "a" + "?" * 22 + "b" + "?" * 22 + "c"
