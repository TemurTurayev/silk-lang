"""
Tests for number .digitWindowRange3() method - range of sliding windows of size 3.
"""

from silk.interpreter import Interpreter


class TestNumberDigitWindowRange3:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitWindowRange3_basic(self):
        output = self._run('print(15324.digitWindowRange3())')
        # max-min: (5-1), (5-2), (4-2) = [4, 3, 2]
        assert output[-1] == "[4, 3, 2]"

    def test_digitWindowRange3_same(self):
        output = self._run('print(1111.digitWindowRange3())')
        # [0, 0]
        assert output[-1] == "[0, 0]"
