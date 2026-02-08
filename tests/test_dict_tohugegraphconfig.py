"""
Tests for dict .toHugeGraphConfig() method - HugeGraph config format.
"""

from silk.interpreter import Interpreter


class TestDictToHugeGraphConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHugeGraphConfig_basic(self):
        output = self._run('print({"port": 8080}.toHugeGraphConfig())')
        assert output[-1] == "port = 8080"

    def test_toHugeGraphConfig_multi(self):
        output = self._run('print({"host": "localhost", "port": 8080}.toHugeGraphConfig())')
        assert "host = localhost" in output[-1]
        assert "port = 8080" in output[-1]
