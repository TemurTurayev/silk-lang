"""
Tests for dict .toVaultV2Config() method - Vault v2 config format.
"""

from silk.interpreter import Interpreter


class TestDictToVaultV2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVaultV2Config_basic(self):
        output = self._run('print({"port": 8200}.toVaultV2Config())')
        assert output[-1] == "port = 8200"

    def test_toVaultV2Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 8200}.toVaultV2Config())')
        assert "host = localhost" in output[-1]
        assert "port = 8200" in output[-1]
