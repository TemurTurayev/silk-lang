"""
Tests for array .mapIsOdd() method - check if each element is odd.
"""

from silk.interpreter import Interpreter


class TestArrayMapIsOdd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIsOdd_mixed(self):
        output = self._run('print([1, 2, 3, 4].mapIsOdd())')
        assert output[-1] == "[true, false, true, false]"

    def test_mapIsOdd_allOdd(self):
        output = self._run('print([1, 3, 5].mapIsOdd())')
        assert output[-1] == "[true, true, true]"
