"""
Tests for array .stddev() method.
"""

from silk.interpreter import Interpreter


class TestArrayStddev:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_stddev_basic(self):
        output = self._run('print([2, 4, 4, 4, 5, 5, 7, 9].stddev())')
        assert output[-1] == "2"

    def test_stddev_same(self):
        output = self._run('print([5, 5, 5].stddev())')
        assert output[-1] == "0"

    def test_stddev_pair(self):
        output = self._run('print([0, 10].stddev())')
        assert output[-1] == "5"
