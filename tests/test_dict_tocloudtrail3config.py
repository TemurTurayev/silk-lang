"""
Tests for dict .toCloudTrail3Config() method - format as CloudTrail v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCloudTrail3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudTrail3Config_basic(self):
        output = self._run('print({"trail": "management"}.toCloudTrail3Config())')
        assert output[-1] == "trail = management"

    def test_toCloudTrail3Config_multi(self):
        output = self._run('print({"trail": "management", "log": "s3"}.toCloudTrail3Config())')
        assert output[-1] == "trail = management\nlog = s3"
