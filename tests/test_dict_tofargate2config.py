"""
Tests for dict .toFargate2Config() method - format as Fargate config.
"""

from silk.interpreter import Interpreter


class TestDictToFargate2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFargate2Config_basic(self):
        output = self._run('print({"cpu": 256}.toFargate2Config())')
        assert output[-1] == "cpu = 256"

    def test_toFargate2Config_multi(self):
        output = self._run('print({"cpu": 256, "memory": 512}.toFargate2Config())')
        assert "cpu = 256" in output[-1]
