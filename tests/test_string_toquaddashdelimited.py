"""
Tests for string .toQuadDashDelimited() method - split words by ----.
"""

from silk.interpreter import Interpreter


class TestStringToQuadDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadDashDelimited_basic(self):
        output = self._run('print("hello world".toQuadDashDelimited())')
        assert output[-1] == "hello----world"

    def test_toQuadDashDelimited_three(self):
        output = self._run('print("a b c".toQuadDashDelimited())')
        assert output[-1] == "a----b----c"
