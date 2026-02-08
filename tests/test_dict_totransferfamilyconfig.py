"""
Tests for dict .toTransferFamilyConfig() method - format as AWS Transfer Family config.
"""

from silk.interpreter import Interpreter


class TestDictToTransferFamilyConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTransferFamilyConfig_basic(self):
        output = self._run('print({"protocol": "sftp"}.toTransferFamilyConfig())')
        assert output[-1] == "protocol = sftp"

    def test_toTransferFamilyConfig_multi(self):
        output = self._run('print({"protocol": "sftp", "port": "22"}.toTransferFamilyConfig())')
        assert "protocol = sftp" in output[-1]
