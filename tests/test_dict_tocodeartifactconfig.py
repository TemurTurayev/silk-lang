"""
Tests for dict .toCodeArtifactConfig() method - format as CodeArtifact config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeArtifactConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeArtifactConfig_basic(self):
        output = self._run('print({"domain": "packages"}.toCodeArtifactConfig())')
        assert output[-1] == "domain = packages"

    def test_toCodeArtifactConfig_multi(self):
        output = self._run('print({"format": "npm", "scope": "private"}.toCodeArtifactConfig())')
        assert "format = npm" in output[-1]
