"""
Tests for number .digitSliceN() method - get digits from index start to end.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSliceN:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSliceN_basic(self):
        output = self._run('print(12345.digitSliceN(1, 4))')
        assert output[-1] == "[2, 3, 4]"

    def test_digitSliceN_start(self):
        output = self._run('print(98765.digitSliceN(0, 3))')
        assert output[-1] == "[9, 8, 7]"
