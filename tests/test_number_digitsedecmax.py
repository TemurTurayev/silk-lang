"""
Tests for number .digitSedecMax() method - max of each consecutive 16-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSedecMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSedecMax_basic(self):
        output = self._run('print(1234567812345678.digitSedecMax())')
        # max(1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8) = 8
        assert output[-1] == "[8]"

    def test_digitSedecMax_remainder(self):
        output = self._run('print(12345678123456789.digitSedecMax())')
        # max(1..8,1..8)=8, max(9)=9
        assert output[-1] == "[8, 9]"
