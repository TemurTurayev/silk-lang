"""
Tests for string .toWordReverse() method - reverse each word.
"""

from silk.interpreter import Interpreter


class TestStringToWordReverse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toWordReverse_basic(self):
        output = self._run('print("hello world".toWordReverse())')
        assert output[-1] == "olleh dlrow"

    def test_toWordReverse_single(self):
        output = self._run('print("abc".toWordReverse())')
        assert output[-1] == "cba"
