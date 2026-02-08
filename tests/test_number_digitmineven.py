"""
Tests for number .digitMinEven() method - smallest even digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMinEven:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMinEven_basic(self):
        output = self._run('print(2468.digitMinEven())')
        assert output[-1] == "2"

    def test_digitMinEven_mixed(self):
        output = self._run('print(1264.digitMinEven())')
        assert output[-1] == "2"
