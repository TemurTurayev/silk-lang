"""
Tests for number .omega() method - count of distinct prime factors.
"""

from silk.interpreter import Interpreter


class TestNumberOmega:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_omega_12(self):
        output = self._run('print(12.omega())')
        assert output[-1] == "2"

    def test_omega_30(self):
        output = self._run('print(30.omega())')
        assert output[-1] == "3"
