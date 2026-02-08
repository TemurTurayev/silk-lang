"""
Tests for number .isLucky() method - check if number is a lucky number.
Lucky numbers: 1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, ...
"""

from silk.interpreter import Interpreter


class TestNumberIsLucky:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isLucky_7(self):
        output = self._run('print(7.isLucky())')
        assert output[-1] == "true"

    def test_isLucky_5(self):
        output = self._run('print(5.isLucky())')
        assert output[-1] == "false"
