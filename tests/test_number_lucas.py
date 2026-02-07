"""
Tests for number .lucasNumber() method.
"""

from silk.interpreter import Interpreter


class TestNumberLucas:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_lucasNumber_0(self):
        output = self._run('print(0.lucasNumber())')
        assert output[-1] == "2"

    def test_lucasNumber_1(self):
        output = self._run('print(1.lucasNumber())')
        assert output[-1] == "1"

    def test_lucasNumber_5(self):
        output = self._run('print(5.lucasNumber())')
        assert output[-1] == "11"
