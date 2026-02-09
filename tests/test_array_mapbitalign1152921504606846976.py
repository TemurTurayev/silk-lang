"""
Tests for array .mapBitAlign1152921504606846976() method - align up to nearest multiple of 1152921504606846976.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign1152921504606846976:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign1152921504606846976_basic(self):
        output = self._run('print([0, 1, 576460752303423487, 576460752303423488, 1152921504606846976].mapBitAlign1152921504606846976())')
        assert output[-1] == '[0, 1152921504606846976, 1152921504606846976, 1152921504606846976, 1152921504606846976]'

    def test_mapBitAlign1152921504606846976_exact(self):
        output = self._run('print([2305843009213693952, 3458764513820540928].mapBitAlign1152921504606846976())')
        assert output[-1] == '[2305843009213693952, 3458764513820540928]'
