"""
Tests for number .digitTailN() method - get last N digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTailN:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTailN_basic(self):
        output = self._run('print(12345.digitTailN(3))')
        assert output[-1] == "[3, 4, 5]"

    def test_digitTailN_two(self):
        output = self._run('print(9876.digitTailN(2))')
        assert output[-1] == "[7, 6]"
