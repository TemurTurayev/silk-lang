"""
Tests for string .soundex() method.
"""

from silk.interpreter import Interpreter


class TestStringSoundex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_soundex_robert(self):
        output = self._run('print("Robert".soundex())')
        assert output[-1] == "R163"

    def test_soundex_rupert(self):
        output = self._run('print("Rupert".soundex())')
        assert output[-1] == "R163"

    def test_soundex_ashcraft(self):
        output = self._run('print("Ashcraft".soundex())')
        assert output[-1] == "A261"
