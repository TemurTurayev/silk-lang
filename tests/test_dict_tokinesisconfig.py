"""
Tests for dict .toKinesisConfig() method - format as Kinesis config.
"""

from silk.interpreter import Interpreter


class TestDictToKinesisConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKinesisConfig_basic(self):
        output = self._run('print({"stream": "events"}.toKinesisConfig())')
        assert output[-1] == "stream = events"

    def test_toKinesisConfig_multi(self):
        output = self._run('print({"shards": 4, "retention": 24}.toKinesisConfig())')
        assert "retention = 24" in output[-1]
