"""
Tests for string .toDuodecDashDelimited() method - split words by ------------ (12 dashes).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecDashDelimited_basic(self):
        output = self._run('print("hello world".toDuodecDashDelimited())')
        assert output[-1] == "hello------------world"

    def test_toDuodecDashDelimited_three(self):
        output = self._run('print("a b c".toDuodecDashDelimited())')
        assert output[-1] == "a------------b------------c"
