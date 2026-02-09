"""
Tests for dict .toDevOpsGuru2Config() method - format as DevOps Guru v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToDevOpsGuru2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDevOpsGuru2Config_basic(self):
        output = self._run('print({"stack": "myStack"}.toDevOpsGuru2Config())')
        assert output[-1] == "stack = myStack"

    def test_toDevOpsGuru2Config_multi(self):
        output = self._run('print({"stack": "prod", "region": "us-east-1"}.toDevOpsGuru2Config())')
        assert output[-1] == "stack = prod\nregion = us-east-1"
