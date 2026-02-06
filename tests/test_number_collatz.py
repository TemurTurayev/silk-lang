"""
Tests for number .collatz() method (steps to reach 1).
"""

from silk.interpreter import Interpreter


class TestNumberCollatz:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_collatz_1(self):
        output = self._run('print(1.collatz())')
        assert output[-1] == "0"

    def test_collatz_6(self):
        output = self._run('print(6.collatz())')
        assert output[-1] == "8"

    def test_collatz_27(self):
        output = self._run('print(27.collatz())')
        assert output[-1] == "111"
