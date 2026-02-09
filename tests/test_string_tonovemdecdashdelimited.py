"""
Tests for string .toNovemdecDashDelimited() method - join words with 19 dashes.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecDashDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecDashDelimited())')
        assert output[-1] == "hello" + "-" * 19 + "world"

    def test_toNovemdecDashDelimited_three(self):
        output = self._run('print("a b c".toNovemdecDashDelimited())')
        assert output[-1] == "a" + "-" * 19 + "b" + "-" * 19 + "c"
