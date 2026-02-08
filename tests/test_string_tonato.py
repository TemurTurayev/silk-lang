"""
Tests for string .toNato() method - NATO phonetic alphabet conversion.
"""

from silk.interpreter import Interpreter


class TestStringToNato:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNato_ab(self):
        output = self._run('print("AB".toNato())')
        assert output[-1] == "Alfa Bravo"

    def test_toNato_sos(self):
        output = self._run('print("SOS".toNato())')
        assert output[-1] == "Sierra Oscar Sierra"
