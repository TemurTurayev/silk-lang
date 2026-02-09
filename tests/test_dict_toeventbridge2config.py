"""
Tests for dict .toEventBridge2Config() method - format as EventBridge v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToEventBridge2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEventBridge2Config_basic(self):
        output = self._run('print({"bus": "default"}.toEventBridge2Config())')
        assert output[-1] == "bus = default"

    def test_toEventBridge2Config_multi(self):
        output = self._run('print({"bus": "default", "region": "us-east-1"}.toEventBridge2Config())')
        assert output[-1] == "bus = default\nregion = us-east-1"
