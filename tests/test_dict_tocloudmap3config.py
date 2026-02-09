"""
Tests for dict .toCloudMap3Config() method - format dict as CloudMap3 config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudMap3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudMap3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toCloudMap3Config())')
        assert output[-1] == "host = localhost"

    def test_toCloudMap3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toCloudMap3Config())')
        assert output[-1] == "host = localhost\nport = 443"
