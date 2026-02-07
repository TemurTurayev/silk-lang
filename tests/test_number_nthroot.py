"""
Tests for number .nthRoot(n) method.
"""

from silk.interpreter import Interpreter


class TestNumberNthRoot:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_nthRoot_cube(self):
        output = self._run('print(27.nthRoot(3))')
        assert output[-1] == "3"

    def test_nthRoot_square(self):
        output = self._run('print(16.nthRoot(2))')
        assert output[-1] == "4"
