"""
Tests for string .toDuovigintiDashDelimited() method - join words with 22 dashes.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiDashDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiDashDelimited())')
        assert output[-1] == "hello" + "-" * 22 + "world"

    def test_toDuovigintiDashDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiDashDelimited())')
        assert output[-1] == "a" + "-" * 22 + "b" + "-" * 22 + "c"
