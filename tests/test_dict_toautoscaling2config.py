"""
Tests for dict .toAutoScaling2Config() method - format as AutoScaling v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToAutoScaling2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAutoScaling2Config_basic(self):
        output = self._run('print({"min_size": 1}.toAutoScaling2Config())')
        assert output[-1] == "min_size = 1"

    def test_toAutoScaling2Config_multi(self):
        output = self._run('print({"min_size": 1, "max_size": 10}.toAutoScaling2Config())')
        assert output[-1] == "min_size = 1\nmax_size = 10"
