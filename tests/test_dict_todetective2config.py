"""
Tests for dict .toDetective2Config() method - format as Detective v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToDetective2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDetective2Config_basic(self):
        output = self._run('print({"graph": "behavior"}.toDetective2Config())')
        assert output[-1] == "graph = behavior"

    def test_toDetective2Config_multi(self):
        output = self._run('print({"graph": "behavior", "region": "us-east-1"}.toDetective2Config())')
        assert output[-1] == "graph = behavior\nregion = us-east-1"
