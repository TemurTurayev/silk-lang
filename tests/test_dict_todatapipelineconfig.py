"""
Tests for dict .toDataPipelineConfig() method - format as AWS Data Pipeline config.
"""

from silk.interpreter import Interpreter


class TestDictToDataPipelineConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDataPipelineConfig_basic(self):
        output = self._run('print({"name": "pipeline1"}.toDataPipelineConfig())')
        assert output[-1] == "name = pipeline1"

    def test_toDataPipelineConfig_multi(self):
        output = self._run('print({"type": "copy", "schedule": "daily"}.toDataPipelineConfig())')
        assert "type = copy" in output[-1]
