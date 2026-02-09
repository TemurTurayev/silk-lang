"""
Tests for dict .toChime3Config() method - format dict as Chime3 config.
"""

from silk.interpreter import Interpreter


class TestDictToChime3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toChime3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toChime3Config())')
        assert output[-1] == "host = localhost"

    def test_toChime3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toChime3Config())')
        assert output[-1] == "host = localhost\nport = 443"
