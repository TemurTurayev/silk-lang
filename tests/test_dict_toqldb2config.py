"""
Tests for dict .toQLDB2Config() method - format as QLDB v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToQLDB2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQLDB2Config_basic(self):
        output = self._run('print({"ledger": "myLedger"}.toQLDB2Config())')
        assert output[-1] == "ledger = myLedger"

    def test_toQLDB2Config_multi(self):
        output = self._run('print({"ledger": "main", "region": "us-east-1"}.toQLDB2Config())')
        assert output[-1] == "ledger = main\nregion = us-east-1"
