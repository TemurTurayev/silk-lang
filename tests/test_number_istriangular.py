"""
Tests for number .isTriangular() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsTriangular:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isTriangular_true(self):
        output = self._run('print(10.isTriangular())')
        assert output[-1] == "true"

    def test_isTriangular_false(self):
        output = self._run('print(11.isTriangular())')
        assert output[-1] == "false"

    def test_isTriangular_one(self):
        output = self._run('print(1.isTriangular())')
        assert output[-1] == "true"
