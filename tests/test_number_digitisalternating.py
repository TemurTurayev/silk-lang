"""
Tests for number .digitIsAlternating() method - digits alternate even/odd.
"""

from silk.interpreter import Interpreter


class TestNumberDigitIsAlternating:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitIsAlternating_true(self):
        output = self._run('print(1234.digitIsAlternating())')
        assert output[-1] == "true"

    def test_digitIsAlternating_false(self):
        output = self._run('print(1134.digitIsAlternating())')
        assert output[-1] == "false"
