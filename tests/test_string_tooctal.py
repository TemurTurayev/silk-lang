"""
Tests for string .toOctal() method - convert each char to octal representation.
"""

from silk.interpreter import Interpreter


class TestStringToOctal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctal_A(self):
        output = self._run('print("A".toOctal())')
        assert output[-1] == "101"

    def test_toOctal_ab(self):
        output = self._run('print("ab".toOctal())')
        assert output[-1] == "141 142"
