"""
Tests for number .isOre() method - harmonic divisor number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsOre:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isOre_6(self):
        output = self._run('print(6.isOre())')
        assert output[-1] == "true"

    def test_isOre_1(self):
        output = self._run('print(1.isOre())')
        assert output[-1] == "true"

    def test_isOre_5(self):
        output = self._run('print(5.isOre())')
        assert output[-1] == "false"
