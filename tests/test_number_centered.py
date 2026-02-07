"""
Tests for number .centered(k) method - centered k-gonal number.
"""

from silk.interpreter import Interpreter


class TestNumberCentered:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_centered_triangle(self):
        output = self._run('print(3.centered(3))')
        assert output[-1] == "10"

    def test_centered_square(self):
        output = self._run('print(3.centered(4))')
        assert output[-1] == "13"

    def test_centered_hex(self):
        output = self._run('print(2.centered(6))')
        assert output[-1] == "7"
