"""
Tests for number .digitIsAscending() method - check if digits are ascending.
"""

from silk.interpreter import Interpreter


class TestNumberDigitIsAscending:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitIsAscending_true(self):
        output = self._run('print(1234.digitIsAscending())')
        assert output[-1] == "true"

    def test_digitIsAscending_false(self):
        output = self._run('print(4321.digitIsAscending())')
        assert output[-1] == "false"
