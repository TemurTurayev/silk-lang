"""
Tests for dict .toECSConfig() method - format as ECS config.
"""

from silk.interpreter import Interpreter


class TestDictToECSConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toECSConfig_basic(self):
        output = self._run('print({"cluster": "prod"}.toECSConfig())')
        assert output[-1] == "cluster = prod"

    def test_toECSConfig_multi(self):
        output = self._run('print({"cpu": 256, "memory": 512}.toECSConfig())')
        assert "memory = 512" in output[-1]
