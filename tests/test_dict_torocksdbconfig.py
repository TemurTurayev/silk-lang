"""
Tests for dict .toRocksDBConfig() method - RocksDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToRocksDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRocksDBConfig_basic(self):
        output = self._run('print({"path": "/data"}.toRocksDBConfig())')
        assert output[-1] == "path = /data"

    def test_toRocksDBConfig_multi(self):
        output = self._run('print({"path": "/data", "cache": 256}.toRocksDBConfig())')
        assert "path = /data" in output[-1]
        assert "cache = 256" in output[-1]
