"""
Tests for number .digitIsAllOdd() method - check if all digits are odd.
"""

from silk.interpreter import Interpreter


class TestNumberDigitIsAllOdd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitIsAllOdd_true(self):
        output = self._run('print(1357.digitIsAllOdd())')
        assert output[-1] == "true"

    def test_digitIsAllOdd_false(self):
        output = self._run('print(1352.digitIsAllOdd())')
        assert output[-1] == "false"
