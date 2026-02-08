"""
Tests for number .digitWindowSum3() method - sum of sliding windows of size 3.
"""

from silk.interpreter import Interpreter


class TestNumberDigitWindowSum3:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitWindowSum3_basic(self):
        output = self._run('print(12345.digitWindowSum3())')
        # [1+2+3, 2+3+4, 3+4+5] = [6, 9, 12]
        assert output[-1] == "[6, 9, 12]"

    def test_digitWindowSum3_four(self):
        output = self._run('print(1111.digitWindowSum3())')
        # [1+1+1, 1+1+1] = [3, 3]
        assert output[-1] == "[3, 3]"
