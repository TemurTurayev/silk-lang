"""
Tests for dict .toIoTAnalytics2Config() method - format as IoT Analytics config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTAnalytics2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTAnalytics2Config_basic(self):
        output = self._run('print({"channelName": "temp-data"}.toIoTAnalytics2Config())')
        assert output[-1] == "channelName = temp-data"

    def test_toIoTAnalytics2Config_multi(self):
        output = self._run('print({"channelName": "temp-data", "retentionDays": 30}.toIoTAnalytics2Config())')
        assert "channelName = temp-data" in output[-1]
