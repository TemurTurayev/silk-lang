"""
Tests for dict .toECS2Config() method - format as ECS config.
"""

from silk.interpreter import Interpreter


class TestDictToECS2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toECS2Config_basic(self):
        output = self._run('print({"cluster": "my-cluster"}.toECS2Config())')
        assert output[-1] == "cluster = my-cluster"

    def test_toECS2Config_multi(self):
        output = self._run('print({"cluster": "my-cluster", "taskCount": 3}.toECS2Config())')
        assert "cluster = my-cluster" in output[-1]
