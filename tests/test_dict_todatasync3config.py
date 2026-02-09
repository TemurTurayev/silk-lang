"""
Tests for dict .toDataSync3Config() method - format dict as DataSync3 config.
"""

from silk.interpreter import Interpreter


class TestDictToDataSync3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDataSync3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toDataSync3Config())')
        assert output[-1] == "host = localhost"

    def test_toDataSync3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toDataSync3Config())')
        assert output[-1] == "host = localhost\nport = 443"
