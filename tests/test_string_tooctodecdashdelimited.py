"""
Tests for string .toOctodecDashDelimited() method - join words with 18 dashes.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecDashDelimited_basic(self):
        output = self._run('print("hello world".toOctodecDashDelimited())')
        assert output[-1] == "hello" + "-" * 18 + "world"

    def test_toOctodecDashDelimited_three(self):
        output = self._run('print("a b c".toOctodecDashDelimited())')
        assert output[-1] == "a" + "-" * 18 + "b" + "-" * 18 + "c"
