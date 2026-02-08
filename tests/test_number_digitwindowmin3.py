"""
Tests for number .digitWindowMin3() method - min of sliding windows of size 3.
"""

from silk.interpreter import Interpreter


class TestNumberDigitWindowMin3:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitWindowMin3_basic(self):
        output = self._run('print(53124.digitWindowMin3())')
        # min(5,3,1), min(3,1,2), min(1,2,4) = [1, 1, 1]
        assert output[-1] == "[1, 1, 1]"

    def test_digitWindowMin3_ascending(self):
        output = self._run('print(1234.digitWindowMin3())')
        # min(1,2,3), min(2,3,4) = [1, 2]
        assert output[-1] == "[1, 2]"
