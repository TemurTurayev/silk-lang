"""
Tests for string .toBinary() method - convert each char to binary.
"""

from silk.interpreter import Interpreter


class TestStringToBinary:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBinary_ab(self):
        output = self._run('print("ab".toBinary())')
        assert output[-1] == "01100001 01100010"

    def test_toBinary_A(self):
        output = self._run('print("A".toBinary())')
        assert output[-1] == "01000001"
