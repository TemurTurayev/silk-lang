"""
Tests for number .digitIsAllEven() method - check if all digits are even.
"""

from silk.interpreter import Interpreter


class TestNumberDigitIsAllEven:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitIsAllEven_true(self):
        output = self._run('print(2468.digitIsAllEven())')
        assert output[-1] == "true"

    def test_digitIsAllEven_false(self):
        output = self._run('print(2461.digitIsAllEven())')
        assert output[-1] == "false"
