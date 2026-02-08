"""
Tests for dict .toGlacierConfig() method - format as Glacier config.
"""

from silk.interpreter import Interpreter


class TestDictToGlacierConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGlacierConfig_basic(self):
        output = self._run('print({"vault": "backup"}.toGlacierConfig())')
        assert output[-1] == "vault = backup"

    def test_toGlacierConfig_multi(self):
        output = self._run('print({"tier": "standard", "days": 30}.toGlacierConfig())')
        assert "tier = standard" in output[-1]
