"""
Tests for array .everyNth(n) method - take every nth element.
"""

from silk.interpreter import Interpreter


class TestArrayEveryNth:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_everyNth_2(self):
        output = self._run('print([1, 2, 3, 4, 5, 6].everyNth(2))')
        assert output[-1] == "[2, 4, 6]"

    def test_everyNth_3(self):
        output = self._run('print([1, 2, 3, 4, 5, 6].everyNth(3))')
        assert output[-1] == "[3, 6]"
