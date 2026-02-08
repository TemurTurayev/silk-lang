"""
Tests for number .radical() method - product of distinct prime factors.
"""

from silk.interpreter import Interpreter


class TestNumberRadical:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_radical_12(self):
        output = self._run('print(12.radical())')
        assert output[-1] == "6"

    def test_radical_30(self):
        output = self._run('print(30.radical())')
        assert output[-1] == "30"
