"""
Tests for array .mapZScore() method - z-score normalization.
"""

from silk.interpreter import Interpreter


class TestArrayMapZScore:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapZScore_basic(self):
        output = self._run('print([2, 4, 4, 4, 5, 5, 7, 9].mapZScore())')
        # Mean=5, StdDev=2 => first element z = (2-5)/2 = -1.5
        assert output[-1].startswith("[-1.5")

    def test_mapZScore_equal(self):
        output = self._run('print([3, 3, 3].mapZScore())')
        assert output[-1] == "[0, 0, 0]"
