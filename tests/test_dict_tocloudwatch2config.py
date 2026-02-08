"""
Tests for dict .toCloudWatch2Config() method - format as CloudWatch Logs config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudWatch2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudWatch2Config_basic(self):
        output = self._run('print({"logGroup": "/aws/lambda/fn"}.toCloudWatch2Config())')
        assert output[-1] == "logGroup = /aws/lambda/fn"

    def test_toCloudWatch2Config_multi(self):
        output = self._run('print({"logGroup": "/aws/lambda/fn", "retention": 14}.toCloudWatch2Config())')
        assert "logGroup = /aws/lambda/fn" in output[-1]
