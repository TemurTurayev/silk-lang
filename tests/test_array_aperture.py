"""
Tests for array .aperture(n) method - sliding window of size n.
"""

from silk.interpreter import Interpreter


class TestArrayAperture:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_aperture_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].aperture(3))')
        assert output[-1] == "[[1, 2, 3], [2, 3, 4], [3, 4, 5]]"

    def test_aperture_two(self):
        output = self._run('print([1, 2, 3].aperture(2))')
        assert output[-1] == "[[1, 2], [2, 3]]"
