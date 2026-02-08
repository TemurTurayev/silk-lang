"""
Tests for number .nthDigit(n) method - get nth digit of number.
"""

from silk.interpreter import Interpreter


class TestNumberNthDigit:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_nthDigit_0(self):
        output = self._run('print(12345.nthDigit(0))')
        assert output[-1] == "1"

    def test_nthDigit_3(self):
        output = self._run('print(12345.nthDigit(3))')
        assert output[-1] == "4"
