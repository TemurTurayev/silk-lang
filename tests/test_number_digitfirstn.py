"""
Tests for number .digitFirstN(n) method - return first N digits as number.
"""

from silk.interpreter import Interpreter


class TestNumberDigitFirstN:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitFirstN_basic(self):
        output = self._run('print(12345.digitFirstN(3))')
        assert output[-1] == "123"

    def test_digitFirstN_single(self):
        output = self._run('print(98765.digitFirstN(1))')
        assert output[-1] == "9"
