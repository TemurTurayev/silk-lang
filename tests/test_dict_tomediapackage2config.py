"""
Tests for dict .toMediaPackage2Config() method - format as MediaPackage v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToMediaPackage2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaPackage2Config_basic(self):
        output = self._run('print({"endpoint": "live"}.toMediaPackage2Config())')
        assert output[-1] == "endpoint = live"

    def test_toMediaPackage2Config_multi(self):
        output = self._run('print({"endpoint": "live", "origin": "us-east"}.toMediaPackage2Config())')
        assert output[-1] == "endpoint = live\norigin = us-east"
