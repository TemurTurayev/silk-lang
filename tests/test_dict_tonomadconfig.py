"""
Tests for dict .toNomadConfig() method - Nomad config format.
"""

from silk.interpreter import Interpreter


class TestDictToNomadConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNomadConfig_basic(self):
        output = self._run('print({"port": 4646}.toNomadConfig())')
        assert output[-1] == "port = 4646"

    def test_toNomadConfig_multi(self):
        output = self._run('print({"host": "localhost", "port": 4646}.toNomadConfig())')
        assert "host = localhost" in output[-1]
        assert "port = 4646" in output[-1]
