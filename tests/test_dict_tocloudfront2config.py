"""
Tests for dict .toCloudFront2Config() method - format as CloudFront v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCloudFront2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudFront2Config_basic(self):
        output = self._run('print({"origin": "s3-bucket"}.toCloudFront2Config())')
        assert output[-1] == "origin = s3-bucket"

    def test_toCloudFront2Config_multi(self):
        output = self._run('print({"origin": "s3-bucket", "ttl": 3600}.toCloudFront2Config())')
        assert output[-1] == "origin = s3-bucket\nttl = 3600"
