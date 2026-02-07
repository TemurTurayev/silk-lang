"""
Tests for number .isEmirp() method - prime whose reverse is also a different prime.
"""

from silk.interpreter import Interpreter


class TestNumberIsEmirp:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isEmirp_13(self):
        output = self._run('print(13.isEmirp())')
        assert output[-1] == "true"

    def test_isEmirp_11(self):
        output = self._run('print(11.isEmirp())')
        assert output[-1] == "false"

    def test_isEmirp_37(self):
        output = self._run('print(37.isEmirp())')
        assert output[-1] == "true"
