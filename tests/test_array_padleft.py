"""
Tests for array .padLeft(n) method - pad with first element to length n.
"""

from silk.interpreter import Interpreter


class TestArrayPadLeft:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_padLeft_basic(self):
        output = self._run('print([1, 2, 3].padLeft(5))')
        assert output[-1] == "[1, 1, 1, 2, 3]"

    def test_padLeft_no_pad(self):
        output = self._run('print([1, 2, 3].padLeft(2))')
        assert output[-1] == "[1, 2, 3]"
