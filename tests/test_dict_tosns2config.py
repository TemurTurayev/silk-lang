"""
Tests for dict .toSNS2Config() method - format as SNS config.
"""

from silk.interpreter import Interpreter


class TestDictToSNS2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSNS2Config_basic(self):
        output = self._run('print({"topicArn": "arn:aws:sns:us-east-1:123:my-topic"}.toSNS2Config())')
        assert output[-1] == "topicArn = arn:aws:sns:us-east-1:123:my-topic"

    def test_toSNS2Config_multi(self):
        output = self._run('print({"topicArn": "my-topic", "protocol": "email"}.toSNS2Config())')
        assert "topicArn = my-topic" in output[-1]
