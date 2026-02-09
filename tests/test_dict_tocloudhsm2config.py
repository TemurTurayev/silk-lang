"""
Tests for dict .toCloudHSM2Config() method - format as CloudHSM v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCloudHSM2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudHSM2Config_basic(self):
        output = self._run('print({"cluster": "hsm01"}.toCloudHSM2Config())')
        assert output[-1] == "cluster = hsm01"

    def test_toCloudHSM2Config_multi(self):
        output = self._run('print({"cluster": "hsm01", "type": "fips"}.toCloudHSM2Config())')
        assert output[-1] == "cluster = hsm01\ntype = fips"
