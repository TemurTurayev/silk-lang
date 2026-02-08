"""
Tests for dict .toEKS2Config() method - format as EKS config.
"""

from silk.interpreter import Interpreter


class TestDictToEKS2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEKS2Config_basic(self):
        output = self._run('print({"clusterName": "prod-eks"}.toEKS2Config())')
        assert output[-1] == "clusterName = prod-eks"

    def test_toEKS2Config_multi(self):
        output = self._run('print({"clusterName": "prod-eks", "version": "1.28"}.toEKS2Config())')
        assert "clusterName = prod-eks" in output[-1]
