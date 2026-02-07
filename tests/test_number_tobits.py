"""
Tests for number .toBits() method.
"""

from silk.interpreter import Interpreter


class TestNumberToBits:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBits_basic(self):
        output = self._run('print(11.toBits())')
        assert output[-1] == "[1, 0, 1, 1]"

    def test_toBits_power_of_2(self):
        output = self._run('print(8.toBits())')
        assert output[-1] == "[1, 0, 0, 0]"

    def test_toBits_one(self):
        output = self._run('print(1.toBits())')
        assert output[-1] == "[1]"
