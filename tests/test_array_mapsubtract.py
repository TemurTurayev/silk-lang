"""
Tests for array .mapSubtract() method - subtract a value from each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapSubtract:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSubtract_basic(self):
        output = self._run('print([10, 20, 30].mapSubtract(5))')
        assert output[-1] == '[5, 15, 25]'

    def test_mapSubtract_large(self):
        output = self._run('print([100, 200, 300].mapSubtract(50))')
        assert output[-1] == '[50, 150, 250]'
