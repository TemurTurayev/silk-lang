"""
Tests for dict .toGunDBConfig() method - GunDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToGunDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGunDBConfig_basic(self):
        output = self._run('print({"port": 8765}.toGunDBConfig())')
        assert output[-1] == "port = 8765"

    def test_toGunDBConfig_multi(self):
        output = self._run('print({"host": "localhost", "port": 8765}.toGunDBConfig())')
        assert "host = localhost" in output[-1]
        assert "port = 8765" in output[-1]
