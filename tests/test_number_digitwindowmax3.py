"""
Tests for number .digitWindowMax3() method - max of sliding windows of size 3.
"""

from silk.interpreter import Interpreter


class TestNumberDigitWindowMax3:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitWindowMax3_basic(self):
        output = self._run('print(13524.digitWindowMax3())')
        # max(1,3,5), max(3,5,2), max(5,2,4) = [5, 5, 5]
        assert output[-1] == "[5, 5, 5]"

    def test_digitWindowMax3_ascending(self):
        output = self._run('print(1234.digitWindowMax3())')
        # max(1,2,3), max(2,3,4) = [3, 4]
        assert output[-1] == "[3, 4]"
