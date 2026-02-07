"""
Tests for number .isPronic() method (n = k*(k+1)).
"""

from silk.interpreter import Interpreter


class TestNumberIsPronic:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPronic_true(self):
        output = self._run('print(6.isPronic())')
        assert output[-1] == "true"

    def test_isPronic_false(self):
        output = self._run('print(7.isPronic())')
        assert output[-1] == "false"

    def test_isPronic_zero(self):
        output = self._run('print(0.isPronic())')
        assert output[-1] == "true"
