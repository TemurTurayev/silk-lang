"""
Tests for string .toTripleEqualDelimited() method - split words by ===.
"""

from silk.interpreter import Interpreter


class TestStringToTripleEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleEqualDelimited_basic(self):
        output = self._run('print("hello world".toTripleEqualDelimited())')
        assert output[-1] == "hello===world"

    def test_toTripleEqualDelimited_three(self):
        output = self._run('print("a b c".toTripleEqualDelimited())')
        assert output[-1] == "a===b===c"
