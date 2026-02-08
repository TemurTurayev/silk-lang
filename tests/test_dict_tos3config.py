"""
Tests for dict .toS3Config() method - format as S3 config.
"""

from silk.interpreter import Interpreter


class TestDictToS3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toS3Config_basic(self):
        output = self._run('print({"bucket": "my-bucket"}.toS3Config())')
        assert output[-1] == "bucket = my-bucket"

    def test_toS3Config_multi(self):
        output = self._run('print({"region": "us-east-1", "versioning": true}.toS3Config())')
        assert "region = us-east-1" in output[-1]
