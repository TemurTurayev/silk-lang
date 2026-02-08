"""
Tests for dict .toCodeBuildConfig() method - format as CodeBuild config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeBuildConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeBuildConfig_basic(self):
        output = self._run('print({"project": "api"}.toCodeBuildConfig())')
        assert output[-1] == "project = api"

    def test_toCodeBuildConfig_multi(self):
        output = self._run('print({"timeout": 60, "compute": "small"}.toCodeBuildConfig())')
        assert "timeout = 60" in output[-1]
