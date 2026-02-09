"""
Tests for dict .toCloudHSM3Config() method - format dict as CloudHSM3 config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudHSM3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudHSM3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toCloudHSM3Config())')
        assert output[-1] == "host = localhost"

    def test_toCloudHSM3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toCloudHSM3Config())')
        assert output[-1] == "host = localhost\nport = 443"
