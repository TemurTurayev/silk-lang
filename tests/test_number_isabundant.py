"""
Tests for number .isAbundant() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsAbundant:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isAbundant_true(self):
        output = self._run('print(12.isAbundant())')
        assert output[-1] == "true"

    def test_isAbundant_false(self):
        output = self._run('print(7.isAbundant())')
        assert output[-1] == "false"

    def test_isAbundant_perfect(self):
        output = self._run('print(6.isAbundant())')
        assert output[-1] == "false"
