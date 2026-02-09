"""
Tests for dict .toIoTEvents3Config() method - format as IoT Events v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToIoTEvents3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTEvents3Config_basic(self):
        output = self._run('print({"detector": "smoke"}.toIoTEvents3Config())')
        assert output[-1] == "detector = smoke"

    def test_toIoTEvents3Config_multi(self):
        output = self._run('print({"detector": "smoke", "severity": "high"}.toIoTEvents3Config())')
        assert output[-1] == "detector = smoke\nseverity = high"
