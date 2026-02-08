"""
Tests for number .digitDecMax() method - max of each consecutive 10-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDecMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDecMax_basic(self):
        output = self._run('print(12345678901234567890.digitDecMax())')
        # [max(1..9,0)=9, max(1..9,0)=9]
        assert output[-1] == "[9, 9]"

    def test_digitDecMax_remainder(self):
        output = self._run('print(123456789012.digitDecMax())')
        # [max(1..9,0)=9, max(1,2)=2]
        assert output[-1] == "[9, 2]"
