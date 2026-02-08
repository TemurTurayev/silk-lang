"""
Tests for dict .toSpannerConfig() method - Cloud Spanner config format.
"""

from silk.interpreter import Interpreter


class TestDictToSpannerConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSpannerConfig_basic(self):
        output = self._run('print({"nodes": 3}.toSpannerConfig())')
        assert output[-1] == "nodes = 3"

    def test_toSpannerConfig_string(self):
        output = self._run('print({"instance": "prod"}.toSpannerConfig())')
        assert output[-1] == "instance = prod"
