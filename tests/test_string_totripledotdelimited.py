"""
Tests for string .toTripleDotDelimited() method - split words by ....
"""

from silk.interpreter import Interpreter


class TestStringToTripleDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleDotDelimited_basic(self):
        output = self._run('print("hello world".toTripleDotDelimited())')
        assert output[-1] == "hello...world"

    def test_toTripleDotDelimited_three(self):
        output = self._run('print("a b c".toTripleDotDelimited())')
        assert output[-1] == "a...b...c"
