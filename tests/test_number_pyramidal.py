"""
Tests for number .pyramidal() method - square pyramidal number n*(n+1)*(2n+1)/6.
"""

from silk.interpreter import Interpreter


class TestNumberPyramidal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pyramidal_1(self):
        output = self._run('print(1.pyramidal())')
        assert output[-1] == "1"

    def test_pyramidal_3(self):
        output = self._run('print(3.pyramidal())')
        assert output[-1] == "14"

    def test_pyramidal_5(self):
        output = self._run('print(5.pyramidal())')
        assert output[-1] == "55"
