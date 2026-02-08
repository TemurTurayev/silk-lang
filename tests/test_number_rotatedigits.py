"""
Tests for number .rotateDigits(n) method - rotate digits left by n.
"""

from silk.interpreter import Interpreter


class TestNumberRotateDigits:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_rotateDigits_1(self):
        output = self._run('print(12345.rotateDigits(1))')
        assert output[-1] == "23451"

    def test_rotateDigits_2(self):
        output = self._run('print(12345.rotateDigits(2))')
        assert output[-1] == "34512"
