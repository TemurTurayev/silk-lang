"""
Tests for dict .toS33Config() method - format as S3 v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToS33Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toS33Config_basic(self):
        output = self._run('print({"bucket": "my-data"}.toS33Config())')
        assert output[-1] == "bucket = my-data"

    def test_toS33Config_multi(self):
        output = self._run('print({"bucket": "my-data", "region": "us-east-1"}.toS33Config())')
        assert output[-1] == "bucket = my-data\nregion = us-east-1"
