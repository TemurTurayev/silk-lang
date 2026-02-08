"""
Tests for dict .toH2Config() method - H2 database config format.
"""

from silk.interpreter import Interpreter


class TestDictToH2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toH2Config_basic(self):
        output = self._run('print({"port": 9092}.toH2Config())')
        assert output[-1] == "port = 9092"

    def test_toH2Config_string(self):
        output = self._run('print({"mode": "embedded"}.toH2Config())')
        assert output[-1] == "mode = embedded"
