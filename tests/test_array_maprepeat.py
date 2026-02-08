"""
Tests for array .mapRepeat(n) method - repeat entire array n times.
"""

from silk.interpreter import Interpreter


class TestArrayMapRepeat:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapRepeat_twice(self):
        output = self._run('print([1, 2].mapRepeat(2))')
        assert output[-1] == "[1, 2, 1, 2]"

    def test_mapRepeat_thrice(self):
        output = self._run('print([3].mapRepeat(3))')
        assert output[-1] == "[3, 3, 3]"
