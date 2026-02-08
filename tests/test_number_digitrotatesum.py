"""
Tests for number .digitRotateSum() method - sum of all digit rotations.
"""

from silk.interpreter import Interpreter


class TestNumberDigitRotateSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitRotateSum_123(self):
        output = self._run('print(123.digitRotateSum())')
        assert output[-1] == "666"

    def test_digitRotateSum_12(self):
        output = self._run('print(12.digitRotateSum())')
        assert output[-1] == "33"
