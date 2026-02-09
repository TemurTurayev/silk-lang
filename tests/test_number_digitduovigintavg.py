"""
Tests for number .digitDuovigintAvg() method - average of each consecutive 22-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuovigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuovigintAvg_basic(self):
        output = self._run('print(2222222222222222222222.digitDuovigintAvg())')
        assert output[-1] == "[2]"

    def test_digitDuovigintAvg_remainder(self):
        output = self._run('print(44444444444444444444446.digitDuovigintAvg())')
        # avg(4*22)=4, avg(6)=6
        assert output[-1] == "[4, 6]"
