"""
Tests for dict .toTimestreamConfig() method - format as Timestream config.
"""

from silk.interpreter import Interpreter


class TestDictToTimestreamConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTimestreamConfig_basic(self):
        output = self._run('print({"database": "mydb"}.toTimestreamConfig())')
        assert output[-1] == "database = mydb"

    def test_toTimestreamConfig_multi(self):
        output = self._run('print({"retention": 24, "magnetic": true}.toTimestreamConfig())')
        assert "retention = 24" in output[-1]
