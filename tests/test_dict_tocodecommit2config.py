"""
Tests for dict .toCodeCommit2Config() method - format as CodeCommit config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeCommit2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeCommit2Config_basic(self):
        output = self._run('print({"repoName": "my-repo"}.toCodeCommit2Config())')
        assert output[-1] == "repoName = my-repo"

    def test_toCodeCommit2Config_multi(self):
        output = self._run('print({"repoName": "my-repo", "branch": "main"}.toCodeCommit2Config())')
        assert "repoName = my-repo" in output[-1]
