"""
Tests for array .uniqueBy(fn) method - unique elements by function result.
"""

from silk.interpreter import Interpreter


class TestArrayUniqueBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_uniqueBy_modulo(self):
        output = self._run('print([1, 2, 3, 4, 5].uniqueBy(|x| x % 3))')
        assert output[-1] == "[1, 2, 3]"

    def test_uniqueBy_length(self):
        output = self._run('print(["a", "bb", "c", "dd"].uniqueBy(|s| s.length))')
        assert output[-1] == "[a, bb]"
