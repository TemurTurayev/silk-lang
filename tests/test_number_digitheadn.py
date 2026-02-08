"""
Tests for number .digitHeadN() method - get first N digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitHeadN:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitHeadN_basic(self):
        output = self._run('print(12345.digitHeadN(3))')
        assert output[-1] == "[1, 2, 3]"

    def test_digitHeadN_two(self):
        output = self._run('print(9876.digitHeadN(2))')
        assert output[-1] == "[9, 8]"
