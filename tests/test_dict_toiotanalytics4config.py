"""
Tests for dict .toIoTAnalytics4Config() method - alias for toGrafanaConfig.
"""

from silk.interpreter import Interpreter


class TestDictToIoTAnalytics4Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTAnalytics4Config_basic(self):
        output = self._run('print({"host": "localhost", "port": 3000}.toIoTAnalytics4Config())')
        assert 'host = localhost' in output[-1]
        assert 'port = 3000' in output[-1]

    def test_toIoTAnalytics4Config_multi(self):
        output = self._run('print({"a": 1, "b": 2, "c": 3}.toIoTAnalytics4Config())')
        assert 'a = 1' in output[-1]
        assert 'c = 3' in output[-1]
