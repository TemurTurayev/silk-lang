"""
Tests for string .toQuattuordecSemicolonDelimited() method - join words with 14 semicolons.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecSemicolonDelimited())')
        assert output[-1] == "hello;;;;;;;;;;;;;;world"

    def test_toQuattuordecSemicolonDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecSemicolonDelimited())')
        assert output[-1] == "a;;;;;;;;;;;;;;b;;;;;;;;;;;;;;c"
