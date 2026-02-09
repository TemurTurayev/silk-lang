"""
Tests for dict .toCloudMap2Config() method - format as CloudMap v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCloudMap2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudMap2Config_basic(self):
        output = self._run('print({"namespace": "prod"}.toCloudMap2Config())')
        assert output[-1] == "namespace = prod"

    def test_toCloudMap2Config_multi(self):
        output = self._run('print({"namespace": "prod", "service": "api"}.toCloudMap2Config())')
        assert output[-1] == "namespace = prod\nservice = api"
