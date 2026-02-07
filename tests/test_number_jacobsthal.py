"""
Tests for number .jacobsthal() method - Jacobsthal number.
"""

from silk.interpreter import Interpreter


class TestNumberJacobsthal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_jacobsthal_0(self):
        output = self._run('print(0.jacobsthal())')
        assert output[-1] == "0"

    def test_jacobsthal_3(self):
        output = self._run('print(3.jacobsthal())')
        assert output[-1] == "3"

    def test_jacobsthal_6(self):
        output = self._run('print(6.jacobsthal())')
        assert output[-1] == "21"
