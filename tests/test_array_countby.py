"""
Tests for array .countBy(fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayCountBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_countBy_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].countBy(|x| x % 2 == 0))')
        assert output[-1] == '{false: 3, true: 2}'

    def test_countBy_strings(self):
        output = self._run('print(["a", "bb", "ccc", "dd"].countBy(|x| x.length))')
        assert output[-1] == '{1: 1, 2: 2, 3: 1}'
