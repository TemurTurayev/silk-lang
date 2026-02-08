"""
Tests for number .digitIsStrictlyDecreasing() method - each digit strictly greater than next.
"""

from silk.interpreter import Interpreter


class TestNumberDigitIsStrictlyDecreasing:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitIsStrictlyDecreasing_true(self):
        output = self._run('print(9531.digitIsStrictlyDecreasing())')
        assert output[-1] == "true"

    def test_digitIsStrictlyDecreasing_false(self):
        output = self._run('print(9551.digitIsStrictlyDecreasing())')
        assert output[-1] == "false"
