"""
Tests for number .digitSextMax() method - max of each consecutive sextuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextMax_basic(self):
        output = self._run('print(123456789012.digitSextMax())')
        # [max(1,2,3,4,5,6)=6, max(7,8,9,0,1,2)=9]
        assert output[-1] == "[6, 9]"

    def test_digitSextMax_remainder(self):
        output = self._run('print(12345679.digitSextMax())')
        # [max(1,2,3,4,5,6)=6, max(7,9)=9]
        assert output[-1] == "[6, 9]"
