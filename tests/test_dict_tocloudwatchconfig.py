"""
Tests for dict .toCloudWatchConfig() method - format as CloudWatch config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudWatchConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudWatchConfig_basic(self):
        output = self._run('print({"namespace": "app"}.toCloudWatchConfig())')
        assert output[-1] == "namespace = app"

    def test_toCloudWatchConfig_multi(self):
        output = self._run('print({"period": 300, "metric": "cpu"}.toCloudWatchConfig())')
        assert "metric = cpu" in output[-1]
