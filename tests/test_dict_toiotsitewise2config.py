"""
Tests for dict .toIoTSiteWise2Config() method - format as IoT SiteWise config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTSiteWise2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTSiteWise2Config_basic(self):
        output = self._run('print({"assetName": "pump-1"}.toIoTSiteWise2Config())')
        assert output[-1] == "assetName = pump-1"

    def test_toIoTSiteWise2Config_multi(self):
        output = self._run('print({"assetName": "pump-1", "modelId": "m-123"}.toIoTSiteWise2Config())')
        assert "assetName = pump-1" in output[-1]
