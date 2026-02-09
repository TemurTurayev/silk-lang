"""
Tests for array .mapBitRoundDown4096() method - round down to nearest multiple of 4096.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown4096:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown4096_basic(self):
        output = self._run('print([1, 4095, 4096, 4097].mapBitRoundDown4096())')
        assert output[-1] == '[0, 0, 4096, 4096]'

    def test_mapBitRoundDown4096_larger(self):
        output = self._run('print([8192, 10000].mapBitRoundDown4096())')
        assert output[-1] == '[8192, 8192]'
