"""
Tests for dict .toSQS3Config() method - format as SQS v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToSQS3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSQS3Config_basic(self):
        output = self._run('print({"queue": "tasks"}.toSQS3Config())')
        assert output[-1] == "queue = tasks"

    def test_toSQS3Config_multi(self):
        output = self._run('print({"queue": "tasks", "timeout": 30}.toSQS3Config())')
        assert output[-1] == "queue = tasks\ntimeout = 30"
