"""
Tests for dict .toEventBridgeConfig() method - format as EventBridge config.
"""

from silk.interpreter import Interpreter


class TestDictToEventBridgeConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEventBridgeConfig_basic(self):
        output = self._run('print({"bus": "default"}.toEventBridgeConfig())')
        assert output[-1] == "bus = default"

    def test_toEventBridgeConfig_multi(self):
        output = self._run('print({"source": "app", "detail": "event"}.toEventBridgeConfig())')
        assert "detail = event" in output[-1]
