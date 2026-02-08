"""
Tests for number .digitOctMax() method - max of each consecutive octuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctMax_basic(self):
        output = self._run('print(1234567812345678.digitOctMax())')
        # [max(1..8)=8, max(1..8)=8]
        assert output[-1] == "[8, 8]"

    def test_digitOctMax_remainder(self):
        output = self._run('print(1234567890.digitOctMax())')
        # [max(1..8)=8, max(9,0)=9]
        assert output[-1] == "[8, 9]"
