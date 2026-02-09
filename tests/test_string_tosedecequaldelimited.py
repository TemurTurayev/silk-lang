"""
Tests for string .toSedecEqualDelimited() method - join words with 16 equals signs.
"""

from silk.interpreter import Interpreter


class TestStringToSedecEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecEqualDelimited_basic(self):
        output = self._run('print("hello world".toSedecEqualDelimited())')
        assert output[-1] == "hello================world"

    def test_toSedecEqualDelimited_three(self):
        output = self._run('print("a b c".toSedecEqualDelimited())')
        assert output[-1] == "a================b================c"
