"""
Tests for array .padRight(n) method - pad with last element to length n.
"""

from silk.interpreter import Interpreter


class TestArrayPadRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_padRight_basic(self):
        output = self._run('print([1, 2, 3].padRight(5))')
        assert output[-1] == "[1, 2, 3, 3, 3]"

    def test_padRight_no_pad(self):
        output = self._run('print([1, 2, 3].padRight(2))')
        assert output[-1] == "[1, 2, 3]"
