"""
Tests for array .isMonotonic() method - either sorted ascending or descending.
"""

from silk.interpreter import Interpreter


class TestArrayIsMonotonic:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isMonotonic_ascending(self):
        output = self._run('print([1, 2, 3, 4].isMonotonic())')
        assert output[-1] == "true"

    def test_isMonotonic_false(self):
        output = self._run('print([1, 3, 2, 4].isMonotonic())')
        assert output[-1] == "false"
