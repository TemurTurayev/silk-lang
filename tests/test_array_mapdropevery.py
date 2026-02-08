"""
Tests for array .mapDropEvery(n) method - drop every nth element.
"""

from silk.interpreter import Interpreter


class TestArrayMapDropEvery:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDropEvery_basic(self):
        output = self._run('print([1, 2, 3, 4, 5, 6].mapDropEvery(3))')
        assert output[-1] == "[1, 2, 4, 5]"

    def test_mapDropEvery_two(self):
        output = self._run('print([1, 2, 3, 4].mapDropEvery(2))')
        assert output[-1] == "[1, 3]"
