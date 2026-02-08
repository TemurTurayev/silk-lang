"""
Tests for number .isHeptagonal() method - heptagonal number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsHeptagonal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isHeptagonal_7(self):
        output = self._run('print(7.isHeptagonal())')
        assert output[-1] == "true"

    def test_isHeptagonal_18(self):
        output = self._run('print(18.isHeptagonal())')
        assert output[-1] == "true"

    def test_isHeptagonal_10(self):
        output = self._run('print(10.isHeptagonal())')
        assert output[-1] == "false"
