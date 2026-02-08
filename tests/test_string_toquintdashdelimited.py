"""
Tests for string .toQuintDashDelimited() method - split words by -----.
"""

from silk.interpreter import Interpreter


class TestStringToQuintDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintDashDelimited_basic(self):
        output = self._run('print("hello world".toQuintDashDelimited())')
        assert output[-1] == "hello-----world"

    def test_toQuintDashDelimited_three(self):
        output = self._run('print("a b c".toQuintDashDelimited())')
        assert output[-1] == "a-----b-----c"
