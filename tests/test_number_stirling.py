"""
Tests for number .stirling() method - Stirling number of the second kind S(n, k).
"""

from silk.interpreter import Interpreter


class TestNumberStirling:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_stirling_4_2(self):
        output = self._run('print(4.stirling(2))')
        assert output[-1] == "7"

    def test_stirling_3_1(self):
        output = self._run('print(3.stirling(1))')
        assert output[-1] == "1"

    def test_stirling_4_4(self):
        output = self._run('print(4.stirling(4))')
        assert output[-1] == "1"
