"""
Tests for number .isProth() method - check if number is a Proth number.
Proth numbers: k * 2^n + 1 where k < 2^n, k is odd.
Examples: 3, 5, 13, 17, 25, 33, 41, 49, 57, 65, ...
"""

from silk.interpreter import Interpreter


class TestNumberIsProth:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isProth_3(self):
        output = self._run('print(3.isProth())')
        assert output[-1] == "true"

    def test_isProth_4(self):
        output = self._run('print(4.isProth())')
        assert output[-1] == "false"
