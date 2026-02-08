"""
Tests for number .digitAt(n) method - get digit at position from right.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAt_0(self):
        output = self._run('print(12345.digitAt(0))')
        assert output[-1] == "5"

    def test_digitAt_2(self):
        output = self._run('print(12345.digitAt(2))')
        assert output[-1] == "3"
