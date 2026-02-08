"""
Tests for number .isCenteredSquare() method - centered square number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsCenteredSquare:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isCenteredSquare_5(self):
        output = self._run('print(5.isCenteredSquare())')
        assert output[-1] == "true"

    def test_isCenteredSquare_13(self):
        output = self._run('print(13.isCenteredSquare())')
        assert output[-1] == "true"

    def test_isCenteredSquare_7(self):
        output = self._run('print(7.isCenteredSquare())')
        assert output[-1] == "false"
