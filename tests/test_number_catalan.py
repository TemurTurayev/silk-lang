"""
Tests for number .catalan() method - Catalan number C(n).
"""

from silk.interpreter import Interpreter


class TestNumberCatalan:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_catalan_0(self):
        output = self._run('print(0.catalan())')
        assert output[-1] == "1"

    def test_catalan_3(self):
        output = self._run('print(3.catalan())')
        assert output[-1] == "5"

    def test_catalan_5(self):
        output = self._run('print(5.catalan())')
        assert output[-1] == "42"
