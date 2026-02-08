"""
Tests for number .digitPower() method - sum of each digit raised to its position power (1-indexed).
"""

from silk.interpreter import Interpreter


class TestNumberDigitPower:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPower_89(self):
        output = self._run('print(89.digitPower())')
        assert output[-1] == "89"

    def test_digitPower_135(self):
        output = self._run('print(135.digitPower())')
        assert output[-1] == "135"

    def test_digitPower_10(self):
        output = self._run('print(10.digitPower())')
        assert output[-1] == "1"
