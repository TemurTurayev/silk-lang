"""
Tests for dict .toMimirConfig() method - Mimir config format.
"""

from silk.interpreter import Interpreter


class TestDictToMimirConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMimirConfig_basic(self):
        output = self._run('print({"port": 9009}.toMimirConfig())')
        assert output[-1] == "port = 9009"

    def test_toMimirConfig_multi(self):
        output = self._run('print({"port": 9009, "storage": "s3"}.toMimirConfig())')
        assert "port = 9009" in output[-1]
        assert "storage = s3" in output[-1]
