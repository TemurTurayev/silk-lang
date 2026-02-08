"""
Tests for string .toAtDelimited() method - split words by at sign.
"""

from silk.interpreter import Interpreter


class TestStringToAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAtDelimited_basic(self):
        output = self._run('print("hello world".toAtDelimited())')
        assert output[-1] == "hello@world"

    def test_toAtDelimited_three(self):
        output = self._run('print("a b c".toAtDelimited())')
        assert output[-1] == "a@b@c"
