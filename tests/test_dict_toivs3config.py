"""
Tests for dict .toIVS3Config() method - format dict as IVS3 config.
"""

from silk.interpreter import Interpreter


class TestDictToIVS3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIVS3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toIVS3Config())')
        assert output[-1] == "host = localhost"

    def test_toIVS3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toIVS3Config())')
        assert output[-1] == "host = localhost\nport = 443"
