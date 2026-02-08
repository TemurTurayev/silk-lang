"""
Tests for number .isOctagonal() method - octagonal number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsOctagonal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isOctagonal_8(self):
        output = self._run('print(8.isOctagonal())')
        assert output[-1] == "true"

    def test_isOctagonal_21(self):
        output = self._run('print(21.isOctagonal())')
        assert output[-1] == "true"

    def test_isOctagonal_10(self):
        output = self._run('print(10.isOctagonal())')
        assert output[-1] == "false"
