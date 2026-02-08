"""
Tests for array .mapModulo() method - compute modulo of each element by given value.
"""

from silk.interpreter import Interpreter


class TestArrayMapModulo:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapModulo_basic(self):
        output = self._run('print([10, 15, 20, 25].mapModulo(7))')
        assert output[-1] == '[3, 1, 6, 4]'

    def test_mapModulo_two(self):
        output = self._run('print([1, 2, 3, 4, 5].mapModulo(3))')
        assert output[-1] == '[1, 2, 0, 1, 2]'
