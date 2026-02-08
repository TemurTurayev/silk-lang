"""
Tests for dict .toPouchDBConfig() method - PouchDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToPouchDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPouchDBConfig_basic(self):
        output = self._run('print({"port": 5984}.toPouchDBConfig())')
        assert output[-1] == "port = 5984"

    def test_toPouchDBConfig_multi(self):
        output = self._run('print({"host": "localhost", "port": 5984}.toPouchDBConfig())')
        assert "host = localhost" in output[-1]
        assert "port = 5984" in output[-1]
