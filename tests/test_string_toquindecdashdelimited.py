"""
Tests for string .toQuindecDashDelimited() method - join words with 15 dashes.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecDashDelimited_basic(self):
        output = self._run('print("hello world".toQuindecDashDelimited())')
        assert output[-1] == "hello---------------world"

    def test_toQuindecDashDelimited_three(self):
        output = self._run('print("a b c".toQuindecDashDelimited())')
        assert output[-1] == "a---------------b---------------c"
