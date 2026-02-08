"""
Tests for dict .toTempoConfig() method - Tempo config format.
"""

from silk.interpreter import Interpreter


class TestDictToTempoConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTempoConfig_basic(self):
        output = self._run('print({"port": 3200}.toTempoConfig())')
        assert output[-1] == "port = 3200"

    def test_toTempoConfig_multi(self):
        output = self._run('print({"port": 3200, "backend": "s3"}.toTempoConfig())')
        assert "port = 3200" in output[-1]
        assert "backend = s3" in output[-1]
