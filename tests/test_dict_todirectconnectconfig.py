"""
Tests for dict .toDirectConnectConfig() method - format as AWS Direct Connect config.
"""

from silk.interpreter import Interpreter


class TestDictToDirectConnectConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDirectConnectConfig_basic(self):
        output = self._run('print({"connection": "dxcon-abc"}.toDirectConnectConfig())')
        assert output[-1] == "connection = dxcon-abc"

    def test_toDirectConnectConfig_multi(self):
        output = self._run('print({"connection": "dxcon-abc", "bandwidth": "1Gbps"}.toDirectConnectConfig())')
        assert "connection = dxcon-abc" in output[-1]
