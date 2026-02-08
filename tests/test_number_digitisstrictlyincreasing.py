"""
Tests for number .digitIsStrictlyIncreasing() method - each digit strictly less than next.
"""

from silk.interpreter import Interpreter


class TestNumberDigitIsStrictlyIncreasing:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitIsStrictlyIncreasing_true(self):
        output = self._run('print(1357.digitIsStrictlyIncreasing())')
        assert output[-1] == "true"

    def test_digitIsStrictlyIncreasing_false(self):
        output = self._run('print(1337.digitIsStrictlyIncreasing())')
        assert output[-1] == "false"
