"""
Tests for dict .toCloudMapConfig() method - format as AWS Cloud Map config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudMapConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudMapConfig_basic(self):
        output = self._run('print({"namespace": "prod"}.toCloudMapConfig())')
        assert output[-1] == "namespace = prod"

    def test_toCloudMapConfig_multi(self):
        output = self._run('print({"namespace": "prod", "service": "api"}.toCloudMapConfig())')
        assert "namespace = prod" in output[-1]
