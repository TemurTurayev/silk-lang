"""
Tests for string .toTriplePlusDelimited() method - split words by +++.
"""

from silk.interpreter import Interpreter


class TestStringToTriplePlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTriplePlusDelimited_basic(self):
        output = self._run('print("hello world".toTriplePlusDelimited())')
        assert output[-1] == "hello+++world"

    def test_toTriplePlusDelimited_three(self):
        output = self._run('print("a b c".toTriplePlusDelimited())')
        assert output[-1] == "a+++b+++c"
