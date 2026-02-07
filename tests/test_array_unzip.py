"""
Tests for array .unzip() method.
"""

from silk.interpreter import Interpreter


class TestArrayUnzip:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_unzip_basic(self):
        output = self._run('print([[1, "a"], [2, "b"], [3, "c"]].unzip())')
        assert output[-1] == "[[1, 2, 3], [a, b, c]]"

    def test_unzip_single(self):
        output = self._run('print([[1, 2]].unzip())')
        assert output[-1] == "[[1], [2]]"
