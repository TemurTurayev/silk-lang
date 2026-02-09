"""
Tests for dict .toBudgets2Config() method - format as Budgets v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToBudgets2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBudgets2Config_basic(self):
        output = self._run('print({"budget": "monthly"}.toBudgets2Config())')
        assert output[-1] == "budget = monthly"

    def test_toBudgets2Config_multi(self):
        output = self._run('print({"budget": "monthly", "limit": "1000"}.toBudgets2Config())')
        assert output[-1] == "budget = monthly\nlimit = 1000"
