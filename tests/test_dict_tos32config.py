"""
Tests for dict .toS32Config() method - format as S3 config.
"""

from silk.interpreter import Interpreter


class TestDictToS32Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toS32Config_basic(self):
        output = self._run('print({"bucket": "my-bucket"}.toS32Config())')
        assert output[-1] == "bucket = my-bucket"

    def test_toS32Config_multi(self):
        output = self._run('print({"bucket": "my-bucket", "region": "us-east-1"}.toS32Config())')
        assert "bucket = my-bucket" in output[-1]
