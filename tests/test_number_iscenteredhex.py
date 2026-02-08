"""
Tests for number .isCenteredHex() method - centered hexagonal number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsCenteredHex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isCenteredHex_7(self):
        output = self._run('print(7.isCenteredHex())')
        assert output[-1] == "true"

    def test_isCenteredHex_19(self):
        output = self._run('print(19.isCenteredHex())')
        assert output[-1] == "true"

    def test_isCenteredHex_10(self):
        output = self._run('print(10.isCenteredHex())')
        assert output[-1] == "false"
