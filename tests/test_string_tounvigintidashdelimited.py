"""
Tests for string .toUnvigintiDashDelimited() method - join words with 21 dashes.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiDashDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiDashDelimited())')
        assert output[-1] == "hello" + "-" * 21 + "world"

    def test_toUnvigintiDashDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiDashDelimited())')
        assert output[-1] == "a" + "-" * 21 + "b" + "-" * 21 + "c"
