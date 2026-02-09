"""
Tests for number .digitTrevigintAvg() method - average of each consecutive 23-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrevigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrevigintAvg_basic(self):
        output = self._run('print(22222222222222222222222.digitTrevigintAvg())')
        assert output[-1] == "[2]"

    def test_digitTrevigintAvg_remainder(self):
        output = self._run('print(444444444444444444444446.digitTrevigintAvg())')
        # avg(4*23)=4, avg(6)=6
        assert output[-1] == "[4, 6]"
