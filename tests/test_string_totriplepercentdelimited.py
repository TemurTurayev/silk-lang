"""
Tests for string .toTriplePercentDelimited() method - split words by %%%.
"""

from silk.interpreter import Interpreter


class TestStringToTriplePercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTriplePercentDelimited_basic(self):
        output = self._run('print("hello world".toTriplePercentDelimited())')
        assert output[-1] == "hello%%%world"

    def test_toTriplePercentDelimited_three(self):
        output = self._run('print("a b c".toTriplePercentDelimited())')
        assert output[-1] == "a%%%b%%%c"
