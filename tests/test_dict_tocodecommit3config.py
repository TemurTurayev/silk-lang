"""
Tests for dict .toCodeCommit3Config() method - format as CodeCommit v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCodeCommit3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeCommit3Config_basic(self):
        output = self._run('print({"repository": "my-repo"}.toCodeCommit3Config())')
        assert output[-1] == "repository = my-repo"

    def test_toCodeCommit3Config_multi(self):
        output = self._run('print({"repository": "my-repo", "branch": "main"}.toCodeCommit3Config())')
        assert output[-1] == "repository = my-repo\nbranch = main"
