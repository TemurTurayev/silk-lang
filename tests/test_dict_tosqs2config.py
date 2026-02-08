"""
Tests for dict .toSQS2Config() method - format as SQS config.
"""

from silk.interpreter import Interpreter


class TestDictToSQS2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSQS2Config_basic(self):
        output = self._run('print({"queueName": "my-queue"}.toSQS2Config())')
        assert output[-1] == "queueName = my-queue"

    def test_toSQS2Config_multi(self):
        output = self._run('print({"queueName": "my-queue", "visibilityTimeout": 30}.toSQS2Config())')
        assert "queueName = my-queue" in output[-1]
