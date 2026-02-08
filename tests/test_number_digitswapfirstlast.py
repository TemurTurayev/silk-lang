"""
Tests for number .digitSwapFirstLast() method - swap first and last digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSwapFirstLast:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSwapFirstLast_basic(self):
        output = self._run('print(12345.digitSwapFirstLast())')
        assert output[-1] == "52341"

    def test_digitSwapFirstLast_two(self):
        output = self._run('print(91.digitSwapFirstLast())')
        assert output[-1] == "19"
