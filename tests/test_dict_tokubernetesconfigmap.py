"""
Tests for dict .toKubernetesConfigMap() method - Kubernetes ConfigMap format.
"""

from silk.interpreter import Interpreter


class TestDictToKubernetesConfigMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKubernetesConfigMap_basic(self):
        output = self._run('print({"port": 3000}.toKubernetesConfigMap())')
        assert output[-1] == "port = 3000"

    def test_toKubernetesConfigMap_multi(self):
        output = self._run('print({"port": 3000, "host": "0.0.0.0"}.toKubernetesConfigMap())')
        assert "port = 3000" in output[-1]
        assert "host = 0.0.0.0" in output[-1]
