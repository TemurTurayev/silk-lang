"""
Tests for string .toQuadHashDelimited() method - split words by ####.
"""

from silk.interpreter import Interpreter


class TestStringToQuadHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadHashDelimited_basic(self):
        output = self._run('print("hello world".toQuadHashDelimited())')
        assert output[-1] == "hello####world"

    def test_toQuadHashDelimited_three(self):
        output = self._run('print("a b c".toQuadHashDelimited())')
        assert output[-1] == "a####b####c"
