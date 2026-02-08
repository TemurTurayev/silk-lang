"""
Tests for number .digitQuintMax() method - max of each consecutive quintuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintMax_basic(self):
        output = self._run('print(1234567890.digitQuintMax())')
        # [max(1,2,3,4,5)=5, max(6,7,8,9,0)=9]
        assert output[-1] == "[5, 9]"

    def test_digitQuintMax_remainder(self):
        output = self._run('print(1234597.digitQuintMax())')
        # [max(1,2,3,4,5)=5, max(9,7)=9]
        assert output[-1] == "[5, 9]"
