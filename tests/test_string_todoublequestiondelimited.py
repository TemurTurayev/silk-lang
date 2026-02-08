"""
Tests for string .toDoubleQuestionDelimited() method - split words by ??.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleQuestionDelimited_basic(self):
        output = self._run('print("hello world".toDoubleQuestionDelimited())')
        assert output[-1] == "hello??world"

    def test_toDoubleQuestionDelimited_three(self):
        output = self._run('print("a b c".toDoubleQuestionDelimited())')
        assert output[-1] == "a??b??c"
