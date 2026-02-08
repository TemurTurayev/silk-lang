"""
Tests for number .isDecagonal() method - decagonal number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsDecagonal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isDecagonal_10(self):
        output = self._run('print(10.isDecagonal())')
        assert output[-1] == "true"

    def test_isDecagonal_27(self):
        output = self._run('print(27.isDecagonal())')
        assert output[-1] == "true"

    def test_isDecagonal_5(self):
        output = self._run('print(5.isDecagonal())')
        assert output[-1] == "false"
