"""
Tests for string .toSedecDashDelimited() method - join words with 16 dashes.
"""

from silk.interpreter import Interpreter


class TestStringToSedecDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecDashDelimited_basic(self):
        output = self._run('print("hello world".toSedecDashDelimited())')
        assert output[-1] == "hello----------------world"

    def test_toSedecDashDelimited_three(self):
        output = self._run('print("a b c".toSedecDashDelimited())')
        assert output[-1] == "a----------------b----------------c"
