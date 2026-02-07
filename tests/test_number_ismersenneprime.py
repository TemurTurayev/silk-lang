"""
Tests for number .isMersennePrime() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsMersennePrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isMersennePrime_true(self):
        output = self._run('print(31.isMersennePrime())')
        assert output[-1] == "true"

    def test_isMersennePrime_false(self):
        output = self._run('print(15.isMersennePrime())')
        assert output[-1] == "false"
