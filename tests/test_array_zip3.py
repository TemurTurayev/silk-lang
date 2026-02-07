"""
Tests for array .zip3(b, c) method.
"""

from silk.interpreter import Interpreter


class TestArrayZip3:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_zip3_basic(self):
        output = self._run('print([1, 2].zip3(["a", "b"], [true, false]))')
        assert output[-1] == "[[1, a, true], [2, b, false]]"

    def test_zip3_uneven(self):
        output = self._run('print([1, 2, 3].zip3(["a", "b"], [10]))')
        assert output[-1] == "[[1, a, 10]]"
