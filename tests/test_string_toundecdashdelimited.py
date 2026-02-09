"""
Tests for string .toUndecDashDelimited() method - split words by ----------- (11 dashes).
"""

from silk.interpreter import Interpreter


class TestStringToUndecDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecDashDelimited_basic(self):
        output = self._run('print("hello world".toUndecDashDelimited())')
        assert output[-1] == "hello-----------world"

    def test_toUndecDashDelimited_three(self):
        output = self._run('print("a b c".toUndecDashDelimited())')
        assert output[-1] == "a-----------b-----------c"
