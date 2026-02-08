"""
Tests for number .isPronicInRange(max) method - check if number is a pronic number <= max.
"""

from silk.interpreter import Interpreter


class TestNumberIsPronicInRange:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPronicInRange_true(self):
        output = self._run('print(6.isPronicInRange(100))')
        assert output[-1] == "true"

    def test_isPronicInRange_false(self):
        output = self._run('print(7.isPronicInRange(100))')
        assert output[-1] == "false"

    def test_isPronicInRange_42(self):
        output = self._run('print(42.isPronicInRange(50))')
        assert output[-1] == "true"
