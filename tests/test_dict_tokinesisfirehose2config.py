"""
Tests for dict .toKinesisFirehose2Config() method - format as KinesisFirehose v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToKinesisFirehose2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKinesisFirehose2Config_basic(self):
        output = self._run('print({"stream": "events"}.toKinesisFirehose2Config())')
        assert output[-1] == "stream = events"

    def test_toKinesisFirehose2Config_multi(self):
        output = self._run('print({"stream": "events", "region": "us-west-2"}.toKinesisFirehose2Config())')
        assert output[-1] == "stream = events\nregion = us-west-2"
