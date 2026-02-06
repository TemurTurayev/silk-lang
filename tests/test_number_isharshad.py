"""
Tests for number .isHarshad() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsHarshad:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isHarshad_true(self):
        output = self._run('print(18.isHarshad())')
        assert output[-1] == "true"

    def test_isHarshad_false(self):
        output = self._run('print(13.isHarshad())')
        assert output[-1] == "false"

    def test_isHarshad_21(self):
        output = self._run('print(21.isHarshad())')
        assert output[-1] == "true"
