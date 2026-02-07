"""
Tests for number .pentagonal() method - pentagonal number.
"""

from silk.interpreter import Interpreter


class TestNumberPentagonal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pentagonal_1(self):
        output = self._run('print(1.pentagonal())')
        assert output[-1] == "1"

    def test_pentagonal_5(self):
        output = self._run('print(5.pentagonal())')
        assert output[-1] == "35"

    def test_pentagonal_3(self):
        output = self._run('print(3.pentagonal())')
        assert output[-1] == "12"
