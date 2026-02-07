"""
Tests for number .hexagonal() method - hexagonal number n*(2n-1).
"""

from silk.interpreter import Interpreter


class TestNumberHexagonal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_hexagonal_1(self):
        output = self._run('print(1.hexagonal())')
        assert output[-1] == "1"

    def test_hexagonal_3(self):
        output = self._run('print(3.hexagonal())')
        assert output[-1] == "15"

    def test_hexagonal_5(self):
        output = self._run('print(5.hexagonal())')
        assert output[-1] == "45"
