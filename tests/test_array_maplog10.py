"""
Tests for array .mapLog10() method - compute log base 10 of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapLog10:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapLog10_powers(self):
        output = self._run('print([1, 10, 100, 1000].mapLog10())')
        assert output[-1] == '[0, 1, 2, 3]'

    def test_mapLog10_larger(self):
        output = self._run('print([10000, 100000].mapLog10())')
        assert output[-1] == '[4, 5]'
