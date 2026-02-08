"""
Tests for string .toTabDelimited() method - split words by tab.
"""

from silk.interpreter import Interpreter


class TestStringToTabDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTabDelimited_basic(self):
        output = self._run('print("hello world".toTabDelimited())')
        assert output[-1] == "hello\tworld"

    def test_toTabDelimited_three(self):
        output = self._run('print("a b c".toTabDelimited())')
        assert output[-1] == "a\tb\tc"
