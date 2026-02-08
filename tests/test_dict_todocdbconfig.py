"""
Tests for dict .toDocDBConfig() method - format as DocumentDB config.
"""

from silk.interpreter import Interpreter


class TestDictToDocDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDocDBConfig_basic(self):
        output = self._run('print({"cluster": "main"}.toDocDBConfig())')
        assert output[-1] == "cluster = main"

    def test_toDocDBConfig_multi(self):
        output = self._run('print({"engine": "docdb", "instances": 3}.toDocDBConfig())')
        assert "instances = 3" in output[-1]
