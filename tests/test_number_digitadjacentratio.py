"""
Tests for number .digitAdjacentRatio() method - ratio of adjacent digit pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentRatio:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentRatio_basic(self):
        output = self._run('print(264.digitAdjacentRatio())')
        # 2/6, 6/4 = [0.3333333333, 1.5]
        assert "1.5" in output[-1]

    def test_digitAdjacentRatio_integer(self):
        output = self._run('print(248.digitAdjacentRatio())')
        # 2/4=0.5, 4/8=0.5
        assert output[-1] == "[0.5, 0.5]"
