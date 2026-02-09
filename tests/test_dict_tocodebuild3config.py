"""
Tests for dict .toCodeBuild3Config() method - format as CodeBuild v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCodeBuild3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeBuild3Config_basic(self):
        output = self._run('print({"project": "my-build"}.toCodeBuild3Config())')
        assert output[-1] == "project = my-build"

    def test_toCodeBuild3Config_multi(self):
        output = self._run('print({"project": "my-build", "timeout": 60}.toCodeBuild3Config())')
        assert output[-1] == "project = my-build\ntimeout = 60"
