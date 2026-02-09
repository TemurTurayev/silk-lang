"""
Tests for dict .toIoTTwinMaker2Config() method - format as IoT TwinMaker config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTTwinMaker2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTTwinMaker2Config_basic(self):
        output = self._run('print({"workspaceId": "ws-1"}.toIoTTwinMaker2Config())')
        assert output[-1] == "workspaceId = ws-1"

    def test_toIoTTwinMaker2Config_multi(self):
        output = self._run('print({"workspaceId": "ws-1", "sceneId": "scene-1"}.toIoTTwinMaker2Config())')
        assert "workspaceId = ws-1" in output[-1]
