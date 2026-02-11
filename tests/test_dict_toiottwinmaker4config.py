"""
Tests for dict .toIoTTwinMaker4Config() method - alias for toGrafanaConfig.
"""

from silk.interpreter import Interpreter


class TestDictToIoTTwinMaker4Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTTwinMaker4Config_basic(self):
        output = self._run('print({"host": "localhost", "port": 3000}.toIoTTwinMaker4Config())')
        assert 'host = localhost' in output[-1]
        assert 'port = 3000' in output[-1]

    def test_toIoTTwinMaker4Config_multi(self):
        output = self._run('print({"a": 1, "b": 2, "c": 3}.toIoTTwinMaker4Config())')
        assert 'a = 1' in output[-1]
        assert 'c = 3' in output[-1]
