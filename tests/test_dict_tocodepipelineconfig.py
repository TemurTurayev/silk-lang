"""
Tests for dict .toCodePipelineConfig() method - format as CodePipeline config.
"""

from silk.interpreter import Interpreter


class TestDictToCodePipelineConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodePipelineConfig_basic(self):
        output = self._run('print({"pipeline": "deploy"}.toCodePipelineConfig())')
        assert output[-1] == "pipeline = deploy"

    def test_toCodePipelineConfig_multi(self):
        output = self._run('print({"stages": 3, "source": "github"}.toCodePipelineConfig())')
        assert "stages = 3" in output[-1]
