"""
Tests for string .toTripleUnderscoreDelimited() method - split words by ___.
"""

from silk.interpreter import Interpreter


class TestStringToTripleUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toTripleUnderscoreDelimited())')
        assert output[-1] == "hello___world"

    def test_toTripleUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toTripleUnderscoreDelimited())')
        assert output[-1] == "a___b___c"
