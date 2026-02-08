"""
Tests for number .isAchilles() method - powerful but not a perfect power.
"""

from silk.interpreter import Interpreter


class TestNumberIsAchilles:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isAchilles_72(self):
        output = self._run('print(72.isAchilles())')
        assert output[-1] == "true"

    def test_isAchilles_108(self):
        output = self._run('print(108.isAchilles())')
        assert output[-1] == "true"

    def test_isAchilles_8(self):
        output = self._run('print(8.isAchilles())')
        assert output[-1] == "false"
