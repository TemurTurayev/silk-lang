"""
Tests for string .toDecHashDelimited() method - split words by ########## (10 hashes).
"""

from silk.interpreter import Interpreter


class TestStringToDecHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecHashDelimited_basic(self):
        output = self._run('print("hello world".toDecHashDelimited())')
        assert output[-1] == "hello##########world"

    def test_toDecHashDelimited_three(self):
        output = self._run('print("a b c".toDecHashDelimited())')
        assert output[-1] == "a##########b##########c"
