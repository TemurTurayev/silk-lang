"""
Tests for dict .toPackerConfig() method - Packer config format.
"""

from silk.interpreter import Interpreter


class TestDictToPackerConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPackerConfig_basic(self):
        output = self._run('print({"type": "docker"}.toPackerConfig())')
        assert output[-1] == "type = docker"

    def test_toPackerConfig_multi(self):
        output = self._run('print({"type": "docker", "image": "ubuntu"}.toPackerConfig())')
        assert "type = docker" in output[-1]
        assert "image = ubuntu" in output[-1]
