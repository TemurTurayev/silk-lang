"""
Tests for dict .toIoTGreengrassConfig() method - format as IoT Greengrass config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTGreengrassConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTGreengrassConfig_basic(self):
        output = self._run('print({"core": "edge_device"}.toIoTGreengrassConfig())')
        assert output[-1] == "core = edge_device"

    def test_toIoTGreengrassConfig_multi(self):
        output = self._run('print({"runtime": "python3", "memory": 512}.toIoTGreengrassConfig())')
        assert "memory = 512" in output[-1]
