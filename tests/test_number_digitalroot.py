"""
Tests for number .digitalRoot() method.
"""

from silk.interpreter import Interpreter


class TestNumberDigitalRoot:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitalRoot_multi(self):
        output = self._run('print(942.digitalRoot())')
        assert output[-1] == "6"

    def test_digitalRoot_single(self):
        output = self._run('print(5.digitalRoot())')
        assert output[-1] == "5"

    def test_digitalRoot_zero(self):
        output = self._run('print(0.digitalRoot())')
        assert output[-1] == "0"
