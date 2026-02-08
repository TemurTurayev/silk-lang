"""
Tests for number .isSquareFree() method - check if number has no squared prime factors.
"""

from silk.interpreter import Interpreter


class TestNumberIsSquareFree:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isSquareFree_10(self):
        output = self._run('print(10.isSquareFree())')
        assert output[-1] == "true"

    def test_isSquareFree_12(self):
        output = self._run('print(12.isSquareFree())')
        assert output[-1] == "false"
