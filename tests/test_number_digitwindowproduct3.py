"""
Tests for number .digitWindowProduct3() method - product of sliding windows of size 3.
"""

from silk.interpreter import Interpreter


class TestNumberDigitWindowProduct3:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitWindowProduct3_basic(self):
        output = self._run('print(12345.digitWindowProduct3())')
        # 1*2*3, 2*3*4, 3*4*5 = [6, 24, 60]
        assert output[-1] == "[6, 24, 60]"

    def test_digitWindowProduct3_ones(self):
        output = self._run('print(1111.digitWindowProduct3())')
        # 1*1*1, 1*1*1 = [1, 1]
        assert output[-1] == "[1, 1]"
