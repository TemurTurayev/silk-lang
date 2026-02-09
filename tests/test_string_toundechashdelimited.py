"""
Tests for string .toUndecHashDelimited() method - split words by ########### (11 hashes).
"""

from silk.interpreter import Interpreter


class TestStringToUndecHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecHashDelimited_basic(self):
        output = self._run('print("hello world".toUndecHashDelimited())')
        assert output[-1] == "hello###########world"

    def test_toUndecHashDelimited_three(self):
        output = self._run('print("a b c".toUndecHashDelimited())')
        assert output[-1] == "a###########b###########c"
