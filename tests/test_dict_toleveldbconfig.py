"""
Tests for dict .toLevelDBConfig() method - LevelDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToLevelDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLevelDBConfig_basic(self):
        output = self._run('print({"path": "/data"}.toLevelDBConfig())')
        assert output[-1] == "path = /data"

    def test_toLevelDBConfig_multi(self):
        output = self._run('print({"path": "/data", "cache": 1024}.toLevelDBConfig())')
        assert "path = /data" in output[-1]
        assert "cache = 1024" in output[-1]
