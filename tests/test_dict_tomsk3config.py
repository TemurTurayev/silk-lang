"""
Tests for dict .toMSK3Config() method - format dict as MSK3 config.
"""

from silk.interpreter import Interpreter


class TestDictToMSK3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMSK3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toMSK3Config())')
        assert output[-1] == "host = localhost"

    def test_toMSK3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toMSK3Config())')
        assert output[-1] == "host = localhost\nport = 443"
