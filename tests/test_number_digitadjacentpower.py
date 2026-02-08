"""
Tests for number .digitAdjacentPower() method - first digit raised to power of second.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentPower:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentPower_basic(self):
        output = self._run('print(231.digitAdjacentPower())')
        # 2^3, 3^1 = [8, 3]
        assert output[-1] == "[8, 3]"

    def test_digitAdjacentPower_squares(self):
        output = self._run('print(322.digitAdjacentPower())')
        # 3^2, 2^2 = [9, 4]
        assert output[-1] == "[9, 4]"
