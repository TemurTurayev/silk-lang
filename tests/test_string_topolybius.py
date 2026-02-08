"""
Tests for string .toPolybius() method - Polybius square cipher (5x5 grid coordinates).
"""

from silk.interpreter import Interpreter


class TestStringToPolybius:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPolybius_ab(self):
        output = self._run('print("ab".toPolybius())')
        assert output[-1] == "11 12"

    def test_toPolybius_hi(self):
        output = self._run('print("hi".toPolybius())')
        assert output[-1] == "23 24"
