"""
Tests for number .collatzSequence() method - full sequence to 1.
"""

from silk.interpreter import Interpreter


class TestNumberCollatzSequence:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_collatzSequence_6(self):
        output = self._run('print(6.collatzSequence())')
        assert output[-1] == "[6, 3, 10, 5, 16, 8, 4, 2, 1]"

    def test_collatzSequence_1(self):
        output = self._run('print(1.collatzSequence())')
        assert output[-1] == "[1]"
