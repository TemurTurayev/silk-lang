"""
Tests for string .toMorse() method - convert to Morse code.
"""

from silk.interpreter import Interpreter


class TestStringToMorse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMorse_hello(self):
        output = self._run('print("hello".toMorse())')
        assert output[-1] == ".... . .-.. .-.. ---"

    def test_toMorse_sos(self):
        output = self._run('print("SOS".toMorse())')
        assert output[-1] == "... --- ..."
