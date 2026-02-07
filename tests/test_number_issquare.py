"""
Tests for number .isSquare() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsSquare:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isSquare_true(self):
        output = self._run('print(16.isSquare())')
        assert output[-1] == "true"

    def test_isSquare_false(self):
        output = self._run('print(15.isSquare())')
        assert output[-1] == "false"

    def test_isSquare_one(self):
        output = self._run('print(1.isSquare())')
        assert output[-1] == "true"
