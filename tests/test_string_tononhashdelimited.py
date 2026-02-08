"""
Tests for string .toNonHashDelimited() method - split words by ######### (9 hashes).
"""

from silk.interpreter import Interpreter


class TestStringToNonHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonHashDelimited_basic(self):
        output = self._run('print("hello world".toNonHashDelimited())')
        assert output[-1] == "hello#########world"

    def test_toNonHashDelimited_three(self):
        output = self._run('print("a b c".toNonHashDelimited())')
        assert output[-1] == "a#########b#########c"
