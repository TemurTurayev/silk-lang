"""
Tests for string .toASCIIArt() method - convert chars to ASCII codes.
"""

from silk.interpreter import Interpreter


class TestStringToASCIIArt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toASCIIArt_hi(self):
        output = self._run('print("hi".toASCIIArt())')
        assert output[-1] == "104 105"

    def test_toASCIIArt_AB(self):
        output = self._run('print("AB".toASCIIArt())')
        assert output[-1] == "65 66"
