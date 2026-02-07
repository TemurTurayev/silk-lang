"""
Tests for number .pronic() method - pronic/oblong number n*(n+1).
"""

from silk.interpreter import Interpreter


class TestNumberPronic:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pronic_3(self):
        output = self._run('print(3.pronic())')
        assert output[-1] == "12"

    def test_pronic_5(self):
        output = self._run('print(5.pronic())')
        assert output[-1] == "30"
