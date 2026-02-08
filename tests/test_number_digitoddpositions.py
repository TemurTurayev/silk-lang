"""
Tests for number .digitOddPositions() method - get digits at odd indices (0-based).
"""

from silk.interpreter import Interpreter


class TestNumberDigitOddPositions:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOddPositions_basic(self):
        output = self._run('print(12345.digitOddPositions())')
        # indices 1,3 -> digits 2,4
        assert output[-1] == "[2, 4]"

    def test_digitOddPositions_four(self):
        output = self._run('print(6789.digitOddPositions())')
        # indices 1,3 -> digits 7,9
        assert output[-1] == "[7, 9]"
