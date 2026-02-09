"""
Tests for dict .toControlTower3Config() method - format dict as ControlTower3 config.
"""

from silk.interpreter import Interpreter


class TestDictToControlTower3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toControlTower3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toControlTower3Config())')
        assert output[-1] == "host = localhost"

    def test_toControlTower3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toControlTower3Config())')
        assert output[-1] == "host = localhost\nport = 443"
