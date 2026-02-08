"""
Tests for dict .toSSMConfig() method - format as Systems Manager config.
"""

from silk.interpreter import Interpreter


class TestDictToSSMConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSSMConfig_basic(self):
        output = self._run('print({"parameter": "/app/db"}.toSSMConfig())')
        assert output[-1] == "parameter = /app/db"

    def test_toSSMConfig_multi(self):
        output = self._run('print({"type": "String", "tier": "standard"}.toSSMConfig())')
        assert "type = String" in output[-1]
