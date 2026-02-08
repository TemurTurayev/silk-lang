"""
Tests for dict .toIoTSiteWiseConfig() method - format as IoT SiteWise config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTSiteWiseConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTSiteWiseConfig_basic(self):
        output = self._run('print({"asset": "turbine_01"}.toIoTSiteWiseConfig())')
        assert output[-1] == "asset = turbine_01"

    def test_toIoTSiteWiseConfig_multi(self):
        output = self._run('print({"model": "wind_turbine", "interval": 60}.toIoTSiteWiseConfig())')
        assert "interval = 60" in output[-1]
