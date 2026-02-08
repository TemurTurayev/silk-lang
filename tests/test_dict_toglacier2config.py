"""
Tests for dict .toGlacier2Config() method - format as Glacier config.
"""

from silk.interpreter import Interpreter


class TestDictToGlacier2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGlacier2Config_basic(self):
        output = self._run('print({"vaultName": "my-vault"}.toGlacier2Config())')
        assert output[-1] == "vaultName = my-vault"

    def test_toGlacier2Config_multi(self):
        output = self._run('print({"vaultName": "my-vault", "tier": "Expedited"}.toGlacier2Config())')
        assert "vaultName = my-vault" in output[-1]
