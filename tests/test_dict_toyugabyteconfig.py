"""
Tests for dict .toYugabyteConfig() method - YugabyteDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToYugabyteConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toYugabyteConfig_basic(self):
        output = self._run('print({"port": 5433}.toYugabyteConfig())')
        assert output[-1] == "port = 5433"

    def test_toYugabyteConfig_string(self):
        output = self._run('print({"host": "localhost"}.toYugabyteConfig())')
        assert output[-1] == "host = localhost"
