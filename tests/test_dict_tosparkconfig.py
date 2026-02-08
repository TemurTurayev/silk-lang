"""
Tests for dict .toSparkConfig() method - format as Spark config.
"""

from silk.interpreter import Interpreter


class TestDictToSparkConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSparkConfig_basic(self):
        output = self._run('print({"master": "local"}.toSparkConfig())')
        assert output[-1] == "master = local"

    def test_toSparkConfig_multi(self):
        output = self._run('print({"cores": 8, "shuffle": true}.toSparkConfig())')
        assert "shuffle = true" in output[-1]
