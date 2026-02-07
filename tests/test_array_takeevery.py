"""
Tests for array .takeEvery(n) method.
"""

from silk.interpreter import Interpreter


class TestArrayTakeEvery:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_takeEvery_2(self):
        output = self._run('print([1, 2, 3, 4, 5, 6].takeEvery(2))')
        assert output[-1] == "[1, 3, 5]"

    def test_takeEvery_3(self):
        output = self._run('print([10, 20, 30, 40, 50, 60].takeEvery(3))')
        assert output[-1] == "[10, 40]"

    def test_takeEvery_1(self):
        output = self._run('print([1, 2, 3].takeEvery(1))')
        assert output[-1] == "[1, 2, 3]"
