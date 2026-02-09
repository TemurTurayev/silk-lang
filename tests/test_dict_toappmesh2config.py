"""
Tests for dict .toAppMesh2Config() method - format as AppMesh config.
"""

from silk.interpreter import Interpreter


class TestDictToAppMesh2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppMesh2Config_basic(self):
        output = self._run('print({"meshName": "my-mesh"}.toAppMesh2Config())')
        assert output[-1] == "meshName = my-mesh"

    def test_toAppMesh2Config_multi(self):
        output = self._run('print({"meshName": "my-mesh", "region": "us-east-1"}.toAppMesh2Config())')
        assert "meshName = my-mesh" in output[-1]
