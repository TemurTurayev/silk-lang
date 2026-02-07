"""
Tests for number .isUntouchable() method - not the aliquot sum of any number.
"""

from silk.interpreter import Interpreter


class TestNumberIsUntouchable:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isUntouchable_2(self):
        output = self._run('print(2.isUntouchable())')
        assert output[-1] == "true"

    def test_isUntouchable_5(self):
        output = self._run('print(5.isUntouchable())')
        assert output[-1] == "true"

    def test_isUntouchable_6(self):
        output = self._run('print(6.isUntouchable())')
        assert output[-1] == "false"
