"""
Tests for number .isSelfDescribing() method - self-describing number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsSelfDescribing:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isSelfDescribing_2020(self):
        output = self._run('print(2020.isSelfDescribing())')
        assert output[-1] == "true"

    def test_isSelfDescribing_1210(self):
        output = self._run('print(1210.isSelfDescribing())')
        assert output[-1] == "true"

    def test_isSelfDescribing_123(self):
        output = self._run('print(123.isSelfDescribing())')
        assert output[-1] == "false"
