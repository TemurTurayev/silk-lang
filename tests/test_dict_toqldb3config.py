"""
Tests for dict .toQLDB3Config() method - format as QLDB v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToQLDB3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQLDB3Config_basic(self):
        output = self._run('print({"ledger": "finance"}.toQLDB3Config())')
        assert output[-1] == "ledger = finance"

    def test_toQLDB3Config_multi(self):
        output = self._run('print({"ledger": "finance", "mode": "standard"}.toQLDB3Config())')
        assert output[-1] == "ledger = finance\nmode = standard"
