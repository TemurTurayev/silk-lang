"""
Tests for dict .toAppMeshConfig() method - format as App Mesh config.
"""

from silk.interpreter import Interpreter


class TestDictToAppMeshConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppMeshConfig_basic(self):
        output = self._run('print({"mesh": "default"}.toAppMeshConfig())')
        assert output[-1] == "mesh = default"

    def test_toAppMeshConfig_multi(self):
        output = self._run('print({"protocol": "http", "port": 80}.toAppMeshConfig())')
        assert "port = 80" in output[-1]
