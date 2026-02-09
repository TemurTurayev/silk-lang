"""
Tests for dict .toDirectConnect2Config() method - format as DirectConnect v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToDirectConnect2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDirectConnect2Config_basic(self):
        output = self._run('print({"connection": "dx01"}.toDirectConnect2Config())')
        assert output[-1] == "connection = dx01"

    def test_toDirectConnect2Config_multi(self):
        output = self._run('print({"connection": "dx01", "bandwidth": "1Gbps"}.toDirectConnect2Config())')
        assert output[-1] == "connection = dx01\nbandwidth = 1Gbps"
