"""
Tests for number .toBinaryArray(bits) method.
"""

from silk.interpreter import Interpreter


class TestNumberToBinaryArray:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBinaryArray_basic(self):
        output = self._run('print(5.toBinaryArray(4))')
        assert output[-1] == "[0, 1, 0, 1]"

    def test_toBinaryArray_exact(self):
        output = self._run('print(7.toBinaryArray(3))')
        assert output[-1] == "[1, 1, 1]"
