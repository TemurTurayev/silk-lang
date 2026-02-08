"""
Tests for number .digitIsMonotonic() method - all digits are the same.
"""

from silk.interpreter import Interpreter


class TestNumberDigitIsMonotonic:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitIsMonotonic_true(self):
        output = self._run('print(1111.digitIsMonotonic())')
        assert output[-1] == "true"

    def test_digitIsMonotonic_false(self):
        output = self._run('print(1112.digitIsMonotonic())')
        assert output[-1] == "false"
