"""
Tests for dict .toMediaPackageConfig() method - format as AWS MediaPackage config.
"""

from silk.interpreter import Interpreter


class TestDictToMediaPackageConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaPackageConfig_basic(self):
        output = self._run('print({"origin": "live"}.toMediaPackageConfig())')
        assert output[-1] == "origin = live"

    def test_toMediaPackageConfig_multi(self):
        output = self._run('print({"origin": "live", "format": "hls"}.toMediaPackageConfig())')
        assert "origin = live" in output[-1]
