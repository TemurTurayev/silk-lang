"""
Tests for string .toMorseCode() method - convert to Morse code.
"""

from silk.interpreter import Interpreter


class TestStringToMorseCode:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMorseCode_sos(self):
        output = self._run('print("SOS".toMorseCode())')
        assert output[-1] == "... --- ..."

    def test_toMorseCode_hi(self):
        output = self._run('print("HI".toMorseCode())')
        assert output[-1] == ".... .."
