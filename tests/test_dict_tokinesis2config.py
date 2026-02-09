"""
Tests for dict .toKinesis2Config() method - format as Kinesis v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToKinesis2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKinesis2Config_basic(self):
        output = self._run('print({"stream_name": "events"}.toKinesis2Config())')
        assert output[-1] == "stream_name = events"

    def test_toKinesis2Config_multi(self):
        output = self._run('print({"stream_name": "events", "shards": 4}.toKinesis2Config())')
        assert output[-1] == "stream_name = events\nshards = 4"
