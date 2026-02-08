"""
Tests for array .mapFloor() method - floor each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapFloor:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapFloor_basic(self):
        output = self._run('print([1.5, 2.7, 3.1].mapFloor())')
        assert output[-1] == "[1, 2, 3]"

    def test_mapFloor_negative(self):
        output = self._run('print([-1.5, 0.9].mapFloor())')
        assert output[-1] == "[-2, 0]"
