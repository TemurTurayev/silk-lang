"""
Tests for array .windows(n) method.
"""

from silk.interpreter import Interpreter


class TestArrayWindows:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_windows_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].windows(3))')
        assert output[-1] == "[[1, 2, 3], [2, 3, 4], [3, 4, 5]]"

    def test_windows_pairs(self):
        output = self._run('print([1, 2, 3].windows(2))')
        assert output[-1] == "[[1, 2], [2, 3]]"

    def test_windows_full(self):
        output = self._run('print([1, 2, 3].windows(3))')
        assert output[-1] == "[[1, 2, 3]]"
