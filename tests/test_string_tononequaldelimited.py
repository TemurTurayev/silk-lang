"""
Tests for string .toNonEqualDelimited() method - split words by ========= (9 equals).
"""

from silk.interpreter import Interpreter


class TestStringToNonEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonEqualDelimited_basic(self):
        output = self._run('print("hello world".toNonEqualDelimited())')
        assert output[-1] == "hello=========world"

    def test_toNonEqualDelimited_three(self):
        output = self._run('print("a b c".toNonEqualDelimited())')
        assert output[-1] == "a=========b=========c"
