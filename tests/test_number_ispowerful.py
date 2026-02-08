"""
Tests for number .isPowerful() method - powerful number check.
A powerful number has p^2 dividing n for every prime p dividing n.
"""

from silk.interpreter import Interpreter


class TestNumberIsPowerful:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPowerful_8(self):
        output = self._run('print(8.isPowerful())')
        assert output[-1] == "true"

    def test_isPowerful_36(self):
        output = self._run('print(36.isPowerful())')
        assert output[-1] == "true"

    def test_isPowerful_12(self):
        output = self._run('print(12.isPowerful())')
        assert output[-1] == "false"
