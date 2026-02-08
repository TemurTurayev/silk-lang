"""
Tests for dict .toBadgerDBConfig() method - BadgerDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToBadgerDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBadgerDBConfig_basic(self):
        output = self._run('print({"dir": "/data"}.toBadgerDBConfig())')
        assert output[-1] == "dir = /data"

    def test_toBadgerDBConfig_multi(self):
        output = self._run('print({"dir": "/data", "sync": true}.toBadgerDBConfig())')
        assert "dir = /data" in output[-1]
        assert "sync = true" in output[-1]
