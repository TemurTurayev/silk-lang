"""
Tests for dict .toBudgetsConfig() method - format as Budgets config.
"""

from silk.interpreter import Interpreter


class TestDictToBudgetsConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBudgetsConfig_basic(self):
        output = self._run('print({"limit": "1000"}.toBudgetsConfig())')
        assert output[-1] == "limit = 1000"

    def test_toBudgetsConfig_multi(self):
        output = self._run('print({"type": "cost", "period": "monthly"}.toBudgetsConfig())')
        assert "type = cost" in output[-1]
