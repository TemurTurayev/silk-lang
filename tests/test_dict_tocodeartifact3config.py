"""
Tests for dict .toCodeArtifact3Config() method - format as CodeArtifact v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCodeArtifact3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeArtifact3Config_basic(self):
        output = self._run('print({"domain": "my-domain"}.toCodeArtifact3Config())')
        assert output[-1] == "domain = my-domain"

    def test_toCodeArtifact3Config_multi(self):
        output = self._run('print({"domain": "my-domain", "repository": "npm"}.toCodeArtifact3Config())')
        assert output[-1] == "domain = my-domain\nrepository = npm"
