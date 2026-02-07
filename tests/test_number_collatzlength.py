"""
Tests for number .collatzLength() method - steps in Collatz sequence.
"""

from silk.interpreter import Interpreter


class TestNumberCollatzLength:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_collatzLength_6(self):
        output = self._run('print(6.collatzLength())')
        assert output[-1] == "8"

    def test_collatzLength_1(self):
        output = self._run('print(1.collatzLength())')
        assert output[-1] == "0"
