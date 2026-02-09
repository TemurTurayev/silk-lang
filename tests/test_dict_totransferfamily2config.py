"""
Tests for dict .toTransferFamily2Config() method - format as Transfer Family v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToTransferFamily2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTransferFamily2Config_basic(self):
        output = self._run('print({"protocol": "sftp"}.toTransferFamily2Config())')
        assert output[-1] == "protocol = sftp"

    def test_toTransferFamily2Config_multi(self):
        output = self._run('print({"protocol": "sftp", "endpoint": "public"}.toTransferFamily2Config())')
        assert output[-1] == "protocol = sftp\nendpoint = public"
