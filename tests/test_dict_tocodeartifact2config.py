"""
Tests for dict .toCodeArtifact2Config() method - format as CodeArtifact config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeArtifact2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeArtifact2Config_basic(self):
        output = self._run('print({"domainName": "my-domain"}.toCodeArtifact2Config())')
        assert output[-1] == "domainName = my-domain"

    def test_toCodeArtifact2Config_multi(self):
        output = self._run('print({"domainName": "my-domain", "repoName": "my-repo"}.toCodeArtifact2Config())')
        assert "domainName = my-domain" in output[-1]
