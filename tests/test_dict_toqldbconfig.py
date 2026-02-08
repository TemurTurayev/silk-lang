"""
Tests for dict .toQLDBConfig() method - format as QLDB config.
"""

from silk.interpreter import Interpreter


class TestDictToQLDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQLDBConfig_basic(self):
        output = self._run('print({"ledger": "vehicle_reg"}.toQLDBConfig())')
        assert output[-1] == "ledger = vehicle_reg"

    def test_toQLDBConfig_multi(self):
        output = self._run('print({"deletion": false, "encryption": true}.toQLDBConfig())')
        assert "encryption = true" in output[-1]
