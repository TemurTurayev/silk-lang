"""
Tests for dict .toAppMesh3Config() method - format as App Mesh v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToAppMesh3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppMesh3Config_basic(self):
        output = self._run('print({"mesh": "default"}.toAppMesh3Config())')
        assert output[-1] == "mesh = default"

    def test_toAppMesh3Config_multi(self):
        output = self._run('print({"mesh": "default", "namespace": "prod"}.toAppMesh3Config())')
        assert output[-1] == "mesh = default\nnamespace = prod"
