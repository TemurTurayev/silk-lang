"""
Tests for array .takeRandom(n) method.
"""

from silk.interpreter import Interpreter


class TestArrayTakeRandom:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_takeRandom_length(self):
        output = self._run('print([1, 2, 3, 4, 5].takeRandom(3).length)')
        assert output[-1] == "3"

    def test_takeRandom_single(self):
        output = self._run('print([10].takeRandom(1))')
        assert output[-1] == "[10]"
