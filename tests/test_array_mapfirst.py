"""
Tests for array .mapFirst(fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayMapFirst:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapFirst_basic(self):
        output = self._run('print([1, 2, 3].mapFirst(|x| x * 10))')
        assert output[-1] == "[10, 2, 3]"

    def test_mapFirst_single(self):
        output = self._run('print([5].mapFirst(|x| x + 1))')
        assert output[-1] == "[6]"

    def test_mapFirst_empty(self):
        output = self._run('print([].mapFirst(|x| x * 10))')
        assert output[-1] == "[]"
