"""
Tests for dict .toDataSync2Config() method - format as DataSync v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToDataSync2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDataSync2Config_basic(self):
        output = self._run('print({"task": "transfer"}.toDataSync2Config())')
        assert output[-1] == "task = transfer"

    def test_toDataSync2Config_multi(self):
        output = self._run('print({"task": "transfer", "mode": "full"}.toDataSync2Config())')
        assert output[-1] == "task = transfer\nmode = full"
