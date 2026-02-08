"""
Tests for array .mapZipIndex() method - zip elements with their indices (element first).
"""

from silk.interpreter import Interpreter


class TestArrayMapZipIndex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapZipIndex_basic(self):
        output = self._run('print([10, 20, 30].mapZipIndex())')
        assert output[-1] == "[[10, 0], [20, 1], [30, 2]]"

    def test_mapZipIndex_strings(self):
        output = self._run('print(["a", "b"].mapZipIndex())')
        assert output[-1] == "[[a, 0], [b, 1]]"
