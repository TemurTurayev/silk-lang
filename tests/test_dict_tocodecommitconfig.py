"""
Tests for dict .toCodeCommitConfig() method - format as CodeCommit config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeCommitConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeCommitConfig_basic(self):
        output = self._run('print({"repo": "backend"}.toCodeCommitConfig())')
        assert output[-1] == "repo = backend"

    def test_toCodeCommitConfig_multi(self):
        output = self._run('print({"branch": "main", "triggers": 2}.toCodeCommitConfig())')
        assert "branch = main" in output[-1]
