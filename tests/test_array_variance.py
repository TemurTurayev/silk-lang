"""
Tests for array .variance() method.
"""

from silk.interpreter import Interpreter


class TestArrayVariance:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_variance_basic(self):
        output = self._run('print([2, 4, 4, 4, 5, 5, 7, 9].variance())')
        assert output[-1] == "4"

    def test_variance_same(self):
        output = self._run('print([5, 5, 5].variance())')
        assert output[-1] == "0"

    def test_variance_pair(self):
        output = self._run('print([0, 10].variance())')
        assert output[-1] == "25"
