"""
Tests for number .isWieferich() method - check if number is a Wieferich prime.
Wieferich primes: 1093 and 3511 are the only known ones.
"""

from silk.interpreter import Interpreter


class TestNumberIsWieferich:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isWieferich_1093(self):
        output = self._run('print(1093.isWieferich())')
        assert output[-1] == "true"

    def test_isWieferich_7(self):
        output = self._run('print(7.isWieferich())')
        assert output[-1] == "false"
