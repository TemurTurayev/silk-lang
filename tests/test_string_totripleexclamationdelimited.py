"""
Tests for string .toTripleExclamationDelimited() method - split words by !!!.
"""

from silk.interpreter import Interpreter


class TestStringToTripleExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleExclamationDelimited_basic(self):
        output = self._run('print("hello world".toTripleExclamationDelimited())')
        assert output[-1] == "hello!!!world"

    def test_toTripleExclamationDelimited_three(self):
        output = self._run('print("a b c".toTripleExclamationDelimited())')
        assert output[-1] == "a!!!b!!!c"
