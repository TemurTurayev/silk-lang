"""
Tests for dict .toCloudFormation3Config() method - format dict as CloudFormation3 config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudFormation3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudFormation3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toCloudFormation3Config())')
        assert output[-1] == "host = localhost"

    def test_toCloudFormation3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toCloudFormation3Config())')
        assert output[-1] == "host = localhost\nport = 443"
