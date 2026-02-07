"""
Tests for number .toOctal() method.
"""

from silk.interpreter import Interpreter


class TestNumberToOctal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctal_basic(self):
        output = self._run('print(8.toOctal())')
        assert output[-1] == "10"

    def test_toOctal_larger(self):
        output = self._run('print(255.toOctal())')
        assert output[-1] == "377"

    def test_toOctal_zero(self):
        output = self._run('print(0.toOctal())')
        assert output[-1] == "0"
