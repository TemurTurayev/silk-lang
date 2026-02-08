"""
Tests for number .digitHasZero() method - check if any digit is 0.
"""

from silk.interpreter import Interpreter


class TestNumberDigitHasZero:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitHasZero_true(self):
        output = self._run('print(1024.digitHasZero())')
        assert output[-1] == "true"

    def test_digitHasZero_false(self):
        output = self._run('print(1234.digitHasZero())')
        assert output[-1] == "false"
