"""
Tests for dict .toSSM3Config() method - format dict as SSM3 config.
"""

from silk.interpreter import Interpreter


class TestDictToSSM3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSSM3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toSSM3Config())')
        assert output[-1] == "host = localhost"

    def test_toSSM3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toSSM3Config())')
        assert output[-1] == "host = localhost\nport = 443"
