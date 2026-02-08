"""
Tests for string .toRunLength() method - run-length encode string.
"""

from silk.interpreter import Interpreter


class TestStringToRunLength:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRunLength_basic(self):
        output = self._run('print("aaabbc".toRunLength())')
        assert output[-1] == "a3b2c1"

    def test_toRunLength_single(self):
        output = self._run('print("abc".toRunLength())')
        assert output[-1] == "a1b1c1"
