"""
Tests for number .isCenteredTriangular() method - centered triangular number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsCenteredTriangular:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isCenteredTriangular_4(self):
        output = self._run('print(4.isCenteredTriangular())')
        assert output[-1] == "true"

    def test_isCenteredTriangular_10(self):
        output = self._run('print(10.isCenteredTriangular())')
        assert output[-1] == "true"

    def test_isCenteredTriangular_5(self):
        output = self._run('print(5.isCenteredTriangular())')
        assert output[-1] == "false"
