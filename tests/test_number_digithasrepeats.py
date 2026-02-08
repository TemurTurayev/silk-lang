"""
Tests for number .digitHasRepeats() method - check if any digit appears more than once.
"""

from silk.interpreter import Interpreter


class TestNumberDigitHasRepeats:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitHasRepeats_true(self):
        output = self._run('print(1231.digitHasRepeats())')
        assert output[-1] == "true"

    def test_digitHasRepeats_false(self):
        output = self._run('print(1234.digitHasRepeats())')
        assert output[-1] == "false"
