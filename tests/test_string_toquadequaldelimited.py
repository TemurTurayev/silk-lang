"""
Tests for string .toQuadEqualDelimited() method - split words by ====.
"""

from silk.interpreter import Interpreter


class TestStringToQuadEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadEqualDelimited_basic(self):
        output = self._run('print("hello world".toQuadEqualDelimited())')
        assert output[-1] == "hello====world"

    def test_toQuadEqualDelimited_three(self):
        output = self._run('print("a b c".toQuadEqualDelimited())')
        assert output[-1] == "a====b====c"
