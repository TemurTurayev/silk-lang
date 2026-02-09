"""
Tests for string .toVigintiDashDelimited() method - join words with 20 dashes.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiDashDelimited_basic(self):
        output = self._run('print("hello world".toVigintiDashDelimited())')
        assert output[-1] == "hello--------------------world"

    def test_toVigintiDashDelimited_multi(self):
        output = self._run('print("a b c".toVigintiDashDelimited())')
        assert output[-1] == "a--------------------b--------------------c"
