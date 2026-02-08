"""
Tests for dict .toMediaTailorConfig() method - format as AWS MediaTailor config.
"""

from silk.interpreter import Interpreter


class TestDictToMediaTailorConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaTailorConfig_basic(self):
        output = self._run('print({"adDecisionServer": "ads.example.com"}.toMediaTailorConfig())')
        assert output[-1] == "adDecisionServer = ads.example.com"

    def test_toMediaTailorConfig_multi(self):
        output = self._run('print({"mode": "ssai", "slate": "default"}.toMediaTailorConfig())')
        assert "mode = ssai" in output[-1]
