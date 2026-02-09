"""
Tests for array .mapBitAlign18446744073709551616() method - align up to nearest multiple of 18446744073709551616.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign18446744073709551616:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign18446744073709551616_basic(self):
        output = self._run('print([0, 1, 9223372036854775807, 9223372036854775808, 18446744073709551616].mapBitAlign18446744073709551616())')
        assert output[-1] == '[0, 18446744073709551616, 18446744073709551616, 18446744073709551616, 18446744073709551616]'

    def test_mapBitAlign18446744073709551616_exact(self):
        output = self._run('print([36893488147419103232, 55340232221128654848].mapBitAlign18446744073709551616())')
        assert output[-1] == '[36893488147419103232, 55340232221128654848]'
