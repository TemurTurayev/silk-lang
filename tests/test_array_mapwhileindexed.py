"""
Tests for array .mapWhileIndexed(fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayMapWhileIndexed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapWhileIndexed_all(self):
        output = self._run('print([1, 2, 3].mapWhileIndexed(|i, x| x * 10))')
        assert output[-1] == "[10, 20, 30]"

    def test_mapWhileIndexed_length(self):
        output = self._run('print([1, 2, 3].mapWhileIndexed(|i, x| x).length)')
        assert output[-1] == "3"
