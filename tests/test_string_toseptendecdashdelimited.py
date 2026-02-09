"""
Tests for string .toSeptendecDashDelimited() method - join words with 17 dashes.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecDashDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecDashDelimited())')
        assert output[-1] == "hello" + "-" * 17 + "world"

    def test_toSeptendecDashDelimited_three(self):
        output = self._run('print("a b c".toSeptendecDashDelimited())')
        assert output[-1] == "a" + "-" * 17 + "b" + "-" * 17 + "c"
