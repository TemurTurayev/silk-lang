"""
Tests for array .mapNotNull(fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayMapNotNull:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapNotNull_basic(self):
        output = self._run('print([1, 2, 3, 4].mapNotNull(|x| if x % 2 == 0 then x * 10 else null))')
        assert output[-1] == "[20, 40]"

    def test_mapNotNull_all(self):
        output = self._run('print([1, 2, 3].mapNotNull(|x| x + 1))')
        assert output[-1] == "[2, 3, 4]"
