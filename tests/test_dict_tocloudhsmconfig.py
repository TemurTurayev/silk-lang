"""
Tests for dict .toCloudHSMConfig() method - format as AWS CloudHSM config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudHSMConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudHSMConfig_basic(self):
        output = self._run('print({"cluster": "hsm01"}.toCloudHSMConfig())')
        assert output[-1] == "cluster = hsm01"

    def test_toCloudHSMConfig_multi(self):
        output = self._run('print({"cluster": "hsm01", "region": "us-east-1"}.toCloudHSMConfig())')
        assert "cluster = hsm01" in output[-1]
