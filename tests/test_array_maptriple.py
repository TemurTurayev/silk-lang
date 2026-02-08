"""
Tests for array .mapTriple() method - triple each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapTriple:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapTriple_basic(self):
        output = self._run('print([1, 2, 3].mapTriple())')
        assert output[-1] == "[3, 6, 9]"

    def test_mapTriple_negative(self):
        output = self._run('print([-1, 0, 4].mapTriple())')
        assert output[-1] == "[-3, 0, 12]"
