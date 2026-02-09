"""
Tests for string .toTredecDashDelimited() method - join words with 13 dashes.
"""

from silk.interpreter import Interpreter


class TestStringToTredecDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecDashDelimited_basic(self):
        output = self._run('print("hello world".toTredecDashDelimited())')
        assert output[-1] == "hello-------------world"

    def test_toTredecDashDelimited_three(self):
        output = self._run('print("a b c".toTredecDashDelimited())')
        assert output[-1] == "a-------------b-------------c"
