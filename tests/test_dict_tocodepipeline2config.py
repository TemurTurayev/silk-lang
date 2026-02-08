"""
Tests for dict .toCodePipeline2Config() method - format as CodePipeline config.
"""

from silk.interpreter import Interpreter


class TestDictToCodePipeline2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodePipeline2Config_basic(self):
        output = self._run('print({"pipelineName": "my-pipeline"}.toCodePipeline2Config())')
        assert output[-1] == "pipelineName = my-pipeline"

    def test_toCodePipeline2Config_multi(self):
        output = self._run('print({"pipelineName": "my-pipeline", "version": 1}.toCodePipeline2Config())')
        assert "pipelineName = my-pipeline" in output[-1]
