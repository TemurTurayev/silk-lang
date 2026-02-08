"""
Tests for dict .toImmuDBConfig() method - ImmuDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToImmuDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toImmuDBConfig_basic(self):
        output = self._run('print({"port": 3322}.toImmuDBConfig())')
        assert output[-1] == "port = 3322"

    def test_toImmuDBConfig_string(self):
        output = self._run('print({"dir": "data"}.toImmuDBConfig())')
        assert output[-1] == "dir = data"
