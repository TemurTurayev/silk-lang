"""
Tests for dict .toVagrantConfig() method - Vagrant config format.
"""

from silk.interpreter import Interpreter


class TestDictToVagrantConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVagrantConfig_basic(self):
        output = self._run('print({"box": "ubuntu"}.toVagrantConfig())')
        assert output[-1] == "box = ubuntu"

    def test_toVagrantConfig_multi(self):
        output = self._run('print({"box": "ubuntu", "memory": 1024}.toVagrantConfig())')
        assert "box = ubuntu" in output[-1]
        assert "memory = 1024" in output[-1]
