"""
Tests for dict .toShield3Config() method - format dict as Shield3 config.
"""

from silk.interpreter import Interpreter


class TestDictToShield3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toShield3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toShield3Config())')
        assert output[-1] == "host = localhost"

    def test_toShield3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toShield3Config())')
        assert output[-1] == "host = localhost\nport = 443"
