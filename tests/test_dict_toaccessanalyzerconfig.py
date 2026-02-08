"""
Tests for dict .toAccessAnalyzerConfig() method - format as Access Analyzer config.
"""

from silk.interpreter import Interpreter


class TestDictToAccessAnalyzerConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAccessAnalyzerConfig_basic(self):
        output = self._run('print({"type": "account"}.toAccessAnalyzerConfig())')
        assert output[-1] == "type = account"

    def test_toAccessAnalyzerConfig_multi(self):
        output = self._run('print({"region": "us-east-1", "scope": "all"}.toAccessAnalyzerConfig())')
        assert "region = us-east-1" in output[-1]
