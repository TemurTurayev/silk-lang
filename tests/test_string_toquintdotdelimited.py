"""
Tests for string .toQuintDotDelimited() method - split words by .....
"""

from silk.interpreter import Interpreter


class TestStringToQuintDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintDotDelimited_basic(self):
        output = self._run('print("hello world".toQuintDotDelimited())')
        assert output[-1] == "hello.....world"

    def test_toQuintDotDelimited_three(self):
        output = self._run('print("a b c".toQuintDotDelimited())')
        assert output[-1] == "a.....b.....c"
