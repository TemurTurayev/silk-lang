"""
Tests for number .digitReverse() method - reverse the digits of a number.
"""

from silk.interpreter import Interpreter


class TestNumberDigitReverse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitReverse_123(self):
        output = self._run('print(123.digitReverse())')
        assert output[-1] == "321"

    def test_digitReverse_100(self):
        output = self._run('print(100.digitReverse())')
        assert output[-1] == "1"
