"""
Tests for dict .toKinesisFirehoseConfig() method - format as Kinesis Firehose config.
"""

from silk.interpreter import Interpreter


class TestDictToKinesisFirehoseConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKinesisFirehoseConfig_basic(self):
        output = self._run('print({"deliveryStream": "my-stream"}.toKinesisFirehoseConfig())')
        assert output[-1] == "deliveryStream = my-stream"

    def test_toKinesisFirehoseConfig_multi(self):
        output = self._run('print({"deliveryStream": "my-stream", "bufferSize": 5}.toKinesisFirehoseConfig())')
        assert "deliveryStream = my-stream" in output[-1]
