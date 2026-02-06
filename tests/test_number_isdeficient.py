"""
Tests for number .isDeficient() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsDeficient:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isDeficient_true(self):
        output = self._run('print(8.isDeficient())')
        assert output[-1] == "true"

    def test_isDeficient_false_abundant(self):
        output = self._run('print(12.isDeficient())')
        assert output[-1] == "false"

    def test_isDeficient_false_perfect(self):
        output = self._run('print(6.isDeficient())')
        assert output[-1] == "false"
