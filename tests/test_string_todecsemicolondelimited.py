"""
Tests for string .toDecSemicolonDelimited() method - split words by ;;;;;;;;;; (10 semicolons).
"""

from silk.interpreter import Interpreter


class TestStringToDecSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toDecSemicolonDelimited())')
        assert output[-1] == "hello;;;;;;;;;;world"

    def test_toDecSemicolonDelimited_three(self):
        output = self._run('print("a b c".toDecSemicolonDelimited())')
        assert output[-1] == "a;;;;;;;;;;b;;;;;;;;;;c"
