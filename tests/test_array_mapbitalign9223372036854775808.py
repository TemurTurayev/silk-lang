"""
Tests for array .mapBitAlign9223372036854775808() method - align up to nearest multiple of 9223372036854775808.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign9223372036854775808:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign9223372036854775808_basic(self):
        output = self._run('print([0, 1, 4611686018427387903, 4611686018427387904, 9223372036854775808].mapBitAlign9223372036854775808())')
        assert output[-1] == '[0, 9223372036854775808, 9223372036854775808, 9223372036854775808, 9223372036854775808]'

    def test_mapBitAlign9223372036854775808_exact(self):
        output = self._run('print([18446744073709551616, 27670116110564327424].mapBitAlign9223372036854775808())')
        assert output[-1] == '[18446744073709551616, 27670116110564327424]'
