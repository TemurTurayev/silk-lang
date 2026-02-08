"""
Tests for number .truncateDigits(n) method - keep only first n digits.
"""

from silk.interpreter import Interpreter


class TestNumberTruncateDigits:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_truncateDigits_3(self):
        output = self._run('print(12345.truncateDigits(3))')
        assert output[-1] == "123"

    def test_truncateDigits_1(self):
        output = self._run('print(98765.truncateDigits(1))')
        assert output[-1] == "9"
