"""
Tests for dict .toInspector2Config() method - format as Inspector v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToInspector2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toInspector2Config_basic(self):
        output = self._run('print({"scan_type": "network"}.toInspector2Config())')
        assert output[-1] == "scan_type = network"

    def test_toInspector2Config_multi(self):
        output = self._run('print({"scan_type": "network", "status": "active"}.toInspector2Config())')
        assert output[-1] == "scan_type = network\nstatus = active"
