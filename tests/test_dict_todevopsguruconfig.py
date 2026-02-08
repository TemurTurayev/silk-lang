"""
Tests for dict .toDevOpsGuruConfig() method - format as DevOps Guru config.
"""

from silk.interpreter import Interpreter


class TestDictToDevOpsGuruConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDevOpsGuruConfig_basic(self):
        output = self._run('print({"stack": "production"}.toDevOpsGuruConfig())')
        assert output[-1] == "stack = production"

    def test_toDevOpsGuruConfig_multi(self):
        output = self._run('print({"channel": "sns", "severity": "high"}.toDevOpsGuruConfig())')
        assert "channel = sns" in output[-1]
