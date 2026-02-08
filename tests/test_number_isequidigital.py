"""
Tests for number .isEquidigital() method - factorization uses same digits as n.
"""

from silk.interpreter import Interpreter


class TestNumberIsEquidigital:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isEquidigital_2(self):
        output = self._run('print(2.isEquidigital())')
        assert output[-1] == "true"

    def test_isEquidigital_4(self):
        output = self._run('print(4.isEquidigital())')
        assert output[-1] == "false"
