"""
Tests for string .toOctDashDelimited() method - split words by --------.
"""

from silk.interpreter import Interpreter


class TestStringToOctDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctDashDelimited_basic(self):
        output = self._run('print("hello world".toOctDashDelimited())')
        assert output[-1] == "hello--------world"

    def test_toOctDashDelimited_three(self):
        output = self._run('print("a b c".toOctDashDelimited())')
        assert output[-1] == "a--------b--------c"
