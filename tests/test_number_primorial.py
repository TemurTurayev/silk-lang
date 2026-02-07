"""
Tests for number .primorial() method - product of primes up to n.
"""

from silk.interpreter import Interpreter


class TestNumberPrimorial:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_primorial_5(self):
        output = self._run('print(5.primorial())')
        assert output[-1] == "30"

    def test_primorial_7(self):
        output = self._run('print(7.primorial())')
        assert output[-1] == "210"
