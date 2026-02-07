"""
Tests for number .isCube() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsCube:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isCube_true(self):
        output = self._run('print(27.isCube())')
        assert output[-1] == "true"

    def test_isCube_false(self):
        output = self._run('print(10.isCube())')
        assert output[-1] == "false"

    def test_isCube_one(self):
        output = self._run('print(1.isCube())')
        assert output[-1] == "true"
