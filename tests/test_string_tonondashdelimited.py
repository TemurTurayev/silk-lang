"""
Tests for string .toNonDashDelimited() method - split words by --------- (9 dashes).
"""

from silk.interpreter import Interpreter


class TestStringToNonDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonDashDelimited_basic(self):
        output = self._run('print("hello world".toNonDashDelimited())')
        assert output[-1] == "hello---------world"

    def test_toNonDashDelimited_three(self):
        output = self._run('print("a b c".toNonDashDelimited())')
        assert output[-1] == "a---------b---------c"
