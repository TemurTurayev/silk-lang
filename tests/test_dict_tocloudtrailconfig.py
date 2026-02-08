"""
Tests for dict .toCloudTrailConfig() method - format as CloudTrail config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudTrailConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudTrailConfig_basic(self):
        output = self._run('print({"trail": "main-trail"}.toCloudTrailConfig())')
        assert output[-1] == "trail = main-trail"

    def test_toCloudTrailConfig_multi(self):
        output = self._run('print({"logging": "enabled", "bucket": "audit-logs"}.toCloudTrailConfig())')
        assert "logging = enabled" in output[-1]
