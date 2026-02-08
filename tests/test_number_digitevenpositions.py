"""
Tests for number .digitEvenPositions() method - get digits at even indices (0-based).
"""

from silk.interpreter import Interpreter


class TestNumberDigitEvenPositions:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitEvenPositions_basic(self):
        output = self._run('print(12345.digitEvenPositions())')
        # indices 0,2,4 -> digits 1,3,5
        assert output[-1] == "[1, 3, 5]"

    def test_digitEvenPositions_four(self):
        output = self._run('print(6789.digitEvenPositions())')
        # indices 0,2 -> digits 6,8
        assert output[-1] == "[6, 8]"
