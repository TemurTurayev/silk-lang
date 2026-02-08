"""
Tests for dict .toDockerRunConfig() method - Docker run config format.
"""

from silk.interpreter import Interpreter


class TestDictToDockerRunConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDockerRunConfig_basic(self):
        output = self._run('print({"port": 8080}.toDockerRunConfig())')
        assert output[-1] == "port = 8080"

    def test_toDockerRunConfig_multi(self):
        output = self._run('print({"port": 8080, "name": "app"}.toDockerRunConfig())')
        assert "port = 8080" in output[-1]
        assert "name = app" in output[-1]
