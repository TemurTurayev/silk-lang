"""
Tests for dict .toAthenaConfig() method - format as Athena config.
"""

from silk.interpreter import Interpreter


class TestDictToAthenaConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAthenaConfig_basic(self):
        output = self._run('print({"database": "analytics"}.toAthenaConfig())')
        assert output[-1] == "database = analytics"

    def test_toAthenaConfig_multi(self):
        output = self._run('print({"workgroup": "primary", "output": "s3"}.toAthenaConfig())')
        assert "workgroup = primary" in output[-1]
