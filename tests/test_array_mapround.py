"""
Tests for array .mapRound() method - round each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapRound:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapRound_basic(self):
        output = self._run('print([1.4, 2.6, 3.5].mapRound())')
        assert output[-1] == "[1, 3, 4]"

    def test_mapRound_negative(self):
        output = self._run('print([-1.7, 0.3].mapRound())')
        assert output[-1] == "[-2, 0]"
