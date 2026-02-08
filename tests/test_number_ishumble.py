"""
Tests for number .isHumble() method - check if number is 7-smooth (only prime factors 2,3,5,7).
"""

from silk.interpreter import Interpreter


class TestNumberIsHumble:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isHumble_12(self):
        output = self._run('print(12.isHumble())')
        assert output[-1] == "true"

    def test_isHumble_11(self):
        output = self._run('print(11.isHumble())')
        assert output[-1] == "false"
