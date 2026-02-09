"""
Tests for dict .toAccessAnalyzer2Config() method - format as AccessAnalyzer v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToAccessAnalyzer2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAccessAnalyzer2Config_basic(self):
        output = self._run('print({"analyzer": "default"}.toAccessAnalyzer2Config())')
        assert output[-1] == "analyzer = default"

    def test_toAccessAnalyzer2Config_multi(self):
        output = self._run('print({"analyzer": "default", "type": "account"}.toAccessAnalyzer2Config())')
        assert output[-1] == "analyzer = default\ntype = account"
