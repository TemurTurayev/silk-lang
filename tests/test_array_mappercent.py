"""
Tests for array .mapPercent() method - each element as percentage of total.
"""

from silk.interpreter import Interpreter


class TestArrayMapPercent:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPercent_basic(self):
        output = self._run('print([25, 25, 50].mapPercent())')
        assert output[-1] == "[25, 25, 50]"

    def test_mapPercent_equal(self):
        output = self._run('print([10, 10, 10, 10].mapPercent())')
        assert output[-1] == "[25, 25, 25, 25]"
