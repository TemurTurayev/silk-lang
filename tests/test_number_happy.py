"""
Tests for number .isHappy() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsHappy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isHappy_true(self):
        output = self._run('print(7.isHappy())')
        assert output[-1] == "true"

    def test_isHappy_false(self):
        output = self._run('print(4.isHappy())')
        assert output[-1] == "false"

    def test_isHappy_1(self):
        output = self._run('print(1.isHappy())')
        assert output[-1] == "true"

    def test_isHappy_19(self):
        output = self._run('print(19.isHappy())')
        assert output[-1] == "true"
