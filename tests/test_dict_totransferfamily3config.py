"""
Tests for dict .toTransferFamily3Config() method - format dict as TransferFamily3 config.
"""

from silk.interpreter import Interpreter


class TestDictToTransferFamily3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTransferFamily3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toTransferFamily3Config())')
        assert output[-1] == "host = localhost"

    def test_toTransferFamily3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toTransferFamily3Config())')
        assert output[-1] == "host = localhost\nport = 443"
