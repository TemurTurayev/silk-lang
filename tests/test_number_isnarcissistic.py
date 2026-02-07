"""
Tests for number .isNarcissistic() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsNarcissistic:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isNarcissistic_true(self):
        output = self._run('print(153.isNarcissistic())')
        assert output[-1] == "true"

    def test_isNarcissistic_false(self):
        output = self._run('print(10.isNarcissistic())')
        assert output[-1] == "false"

    def test_isNarcissistic_single_digit(self):
        output = self._run('print(5.isNarcissistic())')
        assert output[-1] == "true"
