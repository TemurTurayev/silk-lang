"""
Tests for string .toSeptQuestionDelimited() method - split words by ???????.
"""

from silk.interpreter import Interpreter


class TestStringToSeptQuestionDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptQuestionDelimited_basic(self):
        output = self._run('print("hello world".toSeptQuestionDelimited())')
        assert output[-1] == "hello???????world"

    def test_toSeptQuestionDelimited_three(self):
        output = self._run('print("a b c".toSeptQuestionDelimited())')
        assert output[-1] == "a???????b???????c"
