"""
Tests for string .toCharCodes() method - array of character codes.
"""

from silk.interpreter import Interpreter


class TestStringToCharCodes:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCharCodes_basic(self):
        output = self._run('print("AB".toCharCodes())')
        assert output[-1] == "[65, 66]"

    def test_toCharCodes_single(self):
        output = self._run('print("a".toCharCodes())')
        assert output[-1] == "[97]"
