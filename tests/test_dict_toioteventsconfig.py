"""
Tests for dict .toIoTEventsConfig() method - format as IoT Events config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTEventsConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTEventsConfig_basic(self):
        output = self._run('print({"detector": "temp_monitor"}.toIoTEventsConfig())')
        assert output[-1] == "detector = temp_monitor"

    def test_toIoTEventsConfig_multi(self):
        output = self._run('print({"state": "active", "timeout": 30}.toIoTEventsConfig())')
        assert "timeout = 30" in output[-1]
