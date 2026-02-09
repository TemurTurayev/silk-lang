"""
Tests for dict .toCodePipeline3Config() method - format as CodePipeline v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCodePipeline3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodePipeline3Config_basic(self):
        output = self._run('print({"pipeline": "deploy"}.toCodePipeline3Config())')
        assert output[-1] == "pipeline = deploy"

    def test_toCodePipeline3Config_multi(self):
        output = self._run('print({"pipeline": "deploy", "stage": "prod"}.toCodePipeline3Config())')
        assert output[-1] == "pipeline = deploy\nstage = prod"
