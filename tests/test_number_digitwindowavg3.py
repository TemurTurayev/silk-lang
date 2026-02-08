"""
Tests for number .digitWindowAvg3() method - average of sliding windows of size 3.
"""

from silk.interpreter import Interpreter


class TestNumberDigitWindowAvg3:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitWindowAvg3_basic(self):
        output = self._run('print(12345.digitWindowAvg3())')
        # (1+2+3)/3, (2+3+4)/3, (3+4+5)/3 = [2, 3, 4]
        assert output[-1] == "[2, 3, 4]"

    def test_digitWindowAvg3_nonInt(self):
        output = self._run('print(1234.digitWindowAvg3())')
        # (1+2+3)/3=2, (2+3+4)/3=3
        assert output[-1] == "[2, 3]"
