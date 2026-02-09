"""
Tests for dict .toFargate3Config() method - format as Fargate v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToFargate3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFargate3Config_basic(self):
        output = self._run('print({"cpu": 256}.toFargate3Config())')
        assert output[-1] == "cpu = 256"

    def test_toFargate3Config_multi(self):
        output = self._run('print({"cpu": 256, "memory": 512}.toFargate3Config())')
        assert output[-1] == "cpu = 256\nmemory = 512"
