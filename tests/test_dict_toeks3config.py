"""
Tests for dict .toEKS3Config() method - format as EKS v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToEKS3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEKS3Config_basic(self):
        output = self._run('print({"cluster": "prod"}.toEKS3Config())')
        assert output[-1] == "cluster = prod"

    def test_toEKS3Config_multi(self):
        output = self._run('print({"cluster": "prod", "nodeGroup": "general"}.toEKS3Config())')
        assert output[-1] == "cluster = prod\nnodeGroup = general"
