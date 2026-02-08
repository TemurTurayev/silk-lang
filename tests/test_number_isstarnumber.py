"""
Tests for number .isStarNumber() method - centered 12-gonal number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsStarNumber:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isStarNumber_13(self):
        output = self._run('print(13.isStarNumber())')
        assert output[-1] == "true"

    def test_isStarNumber_37(self):
        output = self._run('print(37.isStarNumber())')
        assert output[-1] == "true"

    def test_isStarNumber_10(self):
        output = self._run('print(10.isStarNumber())')
        assert output[-1] == "false"
