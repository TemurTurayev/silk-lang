"""
Tests for number .derangements() method - subfactorial !n.
"""

from silk.interpreter import Interpreter


class TestNumberDerangements:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_derangements_0(self):
        output = self._run('print(0.derangements())')
        assert output[-1] == "1"

    def test_derangements_3(self):
        output = self._run('print(3.derangements())')
        assert output[-1] == "2"

    def test_derangements_5(self):
        output = self._run('print(5.derangements())')
        assert output[-1] == "44"
