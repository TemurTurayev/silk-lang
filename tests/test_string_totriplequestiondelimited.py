"""
Tests for string .toTripleQuestionDelimited() method - split words by ???.
"""

from silk.interpreter import Interpreter


class TestStringToTripleQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleQuestionDelimited_basic(self):
        output = self._run('print("hello world".toTripleQuestionDelimited())')
        assert output[-1] == "hello???world"

    def test_toTripleQuestionDelimited_three(self):
        output = self._run('print("a b c".toTripleQuestionDelimited())')
        assert output[-1] == "a???b???c"
