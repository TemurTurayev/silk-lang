"""
Tests for dict .toCloudTrail4Config() method - format dict as CloudTrail4 config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudTrail4Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudTrail4Config_basic(self):
        output = self._run('print({"host": "localhost"}.toCloudTrail4Config())')
        assert output[-1] == "host = localhost"

    def test_toCloudTrail4Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toCloudTrail4Config())')
        assert output[-1] == "host = localhost\nport = 443"
