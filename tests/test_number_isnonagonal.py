"""
Tests for number .isNonagonal() method - nonagonal number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsNonagonal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isNonagonal_9(self):
        output = self._run('print(9.isNonagonal())')
        assert output[-1] == "true"

    def test_isNonagonal_24(self):
        output = self._run('print(24.isNonagonal())')
        assert output[-1] == "true"

    def test_isNonagonal_10(self):
        output = self._run('print(10.isNonagonal())')
        assert output[-1] == "false"
