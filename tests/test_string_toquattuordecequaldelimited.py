"""
Tests for string .toQuattuordecEqualDelimited() method - join words with 14 equals signs.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecEqualDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecEqualDelimited())')
        assert output[-1] == "hello==============world"

    def test_toQuattuordecEqualDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecEqualDelimited())')
        assert output[-1] == "a==============b==============c"
