"""
Tests for array .histogram() method - frequency count.
"""

from silk.interpreter import Interpreter


class TestArrayHistogram:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_histogram_basic(self):
        output = self._run('print([1, 2, 2, 3, 3, 3].histogram().get(3))')
        assert output[-1] == "3"

    def test_histogram_strings(self):
        output = self._run('print(["a", "b", "a"].histogram().get("a"))')
        assert output[-1] == "2"
