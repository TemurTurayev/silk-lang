"""
Tests for number .digitTretrigintProduct() method - product of each consecutive 33-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTretrigintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTretrigintProduct_basic(self):
        output = self._run('print(222222222222222222222222222222222.digitTretrigintProduct())')
        assert output[-1] == "[8589934592]"

    def test_digitTretrigintProduct_remainder(self):
        output = self._run('print(2222222222222222222222222222222223.digitTretrigintProduct())')
        assert output[-1] == "[8589934592, 3]"
