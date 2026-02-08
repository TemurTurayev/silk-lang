"""
Tests for number .coprimesUpTo() method - list all coprimes up to n.
"""

from silk.interpreter import Interpreter


class TestNumberCoprimesUpTo:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_coprimesUpTo_10(self):
        output = self._run('print(10.coprimesUpTo())')
        assert output[-1] == "[1, 3, 7, 9]"

    def test_coprimesUpTo_6(self):
        output = self._run('print(6.coprimesUpTo())')
        assert output[-1] == "[1, 5]"
