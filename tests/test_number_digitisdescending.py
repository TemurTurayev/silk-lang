"""
Tests for number .digitIsDescending() method - check if digits are descending.
"""

from silk.interpreter import Interpreter


class TestNumberDigitIsDescending:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitIsDescending_true(self):
        output = self._run('print(4321.digitIsDescending())')
        assert output[-1] == "true"

    def test_digitIsDescending_false(self):
        output = self._run('print(1234.digitIsDescending())')
        assert output[-1] == "false"
