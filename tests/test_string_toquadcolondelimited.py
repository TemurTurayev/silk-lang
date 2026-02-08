"""
Tests for string .toQuadColonDelimited() method - split words by ::::.
"""

from silk.interpreter import Interpreter


class TestStringToQuadColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadColonDelimited_basic(self):
        output = self._run('print("hello world".toQuadColonDelimited())')
        assert output[-1] == "hello::::world"

    def test_toQuadColonDelimited_three(self):
        output = self._run('print("a b c".toQuadColonDelimited())')
        assert output[-1] == "a::::b::::c"
