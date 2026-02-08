"""
Tests for number .isPyramidal() method - square pyramidal number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsPyramidal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPyramidal_5(self):
        output = self._run('print(5.isPyramidal())')
        assert output[-1] == "true"

    def test_isPyramidal_14(self):
        output = self._run('print(14.isPyramidal())')
        assert output[-1] == "true"

    def test_isPyramidal_7(self):
        output = self._run('print(7.isPyramidal())')
        assert output[-1] == "false"
