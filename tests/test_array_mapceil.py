"""
Tests for array .mapCeil() method - ceiling of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapCeil:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapCeil_basic(self):
        output = self._run('print([1.1, 2.5, 3.9].mapCeil())')
        assert output[-1] == "[2, 3, 4]"

    def test_mapCeil_negative(self):
        output = self._run('print([-1.5, 0.1].mapCeil())')
        assert output[-1] == "[-1, 1]"
