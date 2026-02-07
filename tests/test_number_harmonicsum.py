"""
Tests for number .harmonicSum() method.
"""

from silk.interpreter import Interpreter


class TestNumberHarmonicSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_harmonicSum_one(self):
        output = self._run('print(1.harmonicSum())')
        assert output[-1] == "1"

    def test_harmonicSum_three(self):
        output = self._run('print(3.harmonicSum())')
        # 1 + 1/2 + 1/3 = 11/6 ≈ 1.8333...
        result = float(output[-1])
        assert abs(result - 1.8333333333333333) < 0.0001
