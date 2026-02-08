"""
Tests for array .mapLog2() method - compute log base 2 of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapLog2:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapLog2_powers(self):
        output = self._run('print([1, 2, 4, 8].mapLog2())')
        assert output[-1] == '[0, 1, 2, 3]'

    def test_mapLog2_larger(self):
        output = self._run('print([16, 32, 64].mapLog2())')
        assert output[-1] == '[4, 5, 6]'
