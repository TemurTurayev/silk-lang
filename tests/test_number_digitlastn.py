"""
Tests for number .digitLastN(n) method - return last N digits as number.
"""

from silk.interpreter import Interpreter


class TestNumberDigitLastN:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitLastN_basic(self):
        output = self._run('print(12345.digitLastN(3))')
        assert output[-1] == "345"

    def test_digitLastN_single(self):
        output = self._run('print(98765.digitLastN(1))')
        assert output[-1] == "5"
