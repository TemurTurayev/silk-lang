"""
Tests for dict .toEtcdV3Config() method - etcd v3 config format.
"""

from silk.interpreter import Interpreter


class TestDictToEtcdV3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEtcdV3Config_basic(self):
        output = self._run('print({"port": 2379}.toEtcdV3Config())')
        assert output[-1] == "port = 2379"

    def test_toEtcdV3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 2379}.toEtcdV3Config())')
        assert "host = localhost" in output[-1]
        assert "port = 2379" in output[-1]
