"""
Tests for dict .toCloudFrontConfig() method - format as CloudFront config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudFrontConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudFrontConfig_basic(self):
        output = self._run('print({"origin": "s3bucket"}.toCloudFrontConfig())')
        assert output[-1] == "origin = s3bucket"

    def test_toCloudFrontConfig_multi(self):
        output = self._run('print({"ttl": 86400, "compress": true}.toCloudFrontConfig())')
        assert "compress = true" in output[-1]
