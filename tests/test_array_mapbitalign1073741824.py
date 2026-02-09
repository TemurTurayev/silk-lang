"""
Tests for array .mapBitAlign1073741824() method - align up to nearest multiple of 1073741824.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign1073741824:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign1073741824_basic(self):
        output = self._run('print([0, 1, 536870911, 536870912, 1073741824].mapBitAlign1073741824())')
        assert output[-1] == '[0, 1073741824, 1073741824, 1073741824, 1073741824]'

    def test_mapBitAlign1073741824_exact(self):
        output = self._run('print([2147483648, 3221225472].mapBitAlign1073741824())')
        assert output[-1] == '[2147483648, 3221225472]'
