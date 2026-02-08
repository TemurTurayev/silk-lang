"""
Tests for dict .toBoltDBConfig() method - BoltDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToBoltDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBoltDBConfig_basic(self):
        output = self._run('print({"path": "/data"}.toBoltDBConfig())')
        assert output[-1] == "path = /data"

    def test_toBoltDBConfig_multi(self):
        output = self._run('print({"path": "/data", "timeout": 5}.toBoltDBConfig())')
        assert "path = /data" in output[-1]
        assert "timeout = 5" in output[-1]
