"""
Tests for dict .toCloudFormation2Config() method - format as CloudFormation v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCloudFormation2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudFormation2Config_basic(self):
        output = self._run('print({"stack": "production"}.toCloudFormation2Config())')
        assert output[-1] == "stack = production"

    def test_toCloudFormation2Config_multi(self):
        output = self._run('print({"stack": "production", "region": "us-west-2"}.toCloudFormation2Config())')
        assert output[-1] == "stack = production\nregion = us-west-2"
