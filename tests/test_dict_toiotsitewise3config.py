"""
Tests for dict .toIoTSiteWise3Config() method - format as IoT SiteWise v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToIoTSiteWise3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTSiteWise3Config_basic(self):
        output = self._run('print({"asset": "turbine"}.toIoTSiteWise3Config())')
        assert output[-1] == "asset = turbine"

    def test_toIoTSiteWise3Config_multi(self):
        output = self._run('print({"asset": "turbine", "property": "rpm"}.toIoTSiteWise3Config())')
        assert output[-1] == "asset = turbine\nproperty = rpm"
