"""
Tests for number .digitZeroPad() method - pad digit list to even length with leading zero.
"""

from silk.interpreter import Interpreter


class TestNumberDigitZeroPad:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitZeroPad_odd(self):
        output = self._run('print(123.digitZeroPad())')
        # 3 digits -> pad to 4: [0, 1, 2, 3]
        assert output[-1] == "[0, 1, 2, 3]"

    def test_digitZeroPad_even(self):
        output = self._run('print(1234.digitZeroPad())')
        # 4 digits -> already even: [1, 2, 3, 4]
        assert output[-1] == "[1, 2, 3, 4]"
