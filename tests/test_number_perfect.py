"""
Tests for number .isPerfect() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsPerfect:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPerfect_six(self):
        output = self._run('print(6.isPerfect())')
        assert output[-1] == "true"

    def test_isPerfect_28(self):
        output = self._run('print(28.isPerfect())')
        assert output[-1] == "true"

    def test_isPerfect_12(self):
        output = self._run('print(12.isPerfect())')
        assert output[-1] == "false"

    def test_isPerfect_one(self):
        output = self._run('print(1.isPerfect())')
        assert output[-1] == "false"
