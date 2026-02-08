"""
Tests for dict .toSQSConfig() method - format as SQS config.
"""

from silk.interpreter import Interpreter


class TestDictToSQSConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSQSConfig_basic(self):
        output = self._run('print({"queue": "events"}.toSQSConfig())')
        assert output[-1] == "queue = events"

    def test_toSQSConfig_multi(self):
        output = self._run('print({"delay": 5, "visibility": 30}.toSQSConfig())')
        assert "visibility = 30" in output[-1]
