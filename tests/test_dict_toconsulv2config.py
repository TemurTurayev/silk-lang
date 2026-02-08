"""
Tests for dict .toConsulV2Config() method - Consul v2 config format.
"""

from silk.interpreter import Interpreter


class TestDictToConsulV2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toConsulV2Config_basic(self):
        output = self._run('print({"port": 8500}.toConsulV2Config())')
        assert output[-1] == "port = 8500"

    def test_toConsulV2Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 8500}.toConsulV2Config())')
        assert "host = localhost" in output[-1]
        assert "port = 8500" in output[-1]
