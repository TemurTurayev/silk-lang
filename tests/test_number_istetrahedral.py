"""
Tests for number .isTetrahedral() method - tetrahedral number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsTetrahedral:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isTetrahedral_10(self):
        output = self._run('print(10.isTetrahedral())')
        assert output[-1] == "true"

    def test_isTetrahedral_20(self):
        output = self._run('print(20.isTetrahedral())')
        assert output[-1] == "true"

    def test_isTetrahedral_15(self):
        output = self._run('print(15.isTetrahedral())')
        assert output[-1] == "false"
