"""
Tests for dict .toDataPipeline2Config() method - format as Data Pipeline v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToDataPipeline2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDataPipeline2Config_basic(self):
        output = self._run('print({"pipeline": "etl"}.toDataPipeline2Config())')
        assert output[-1] == "pipeline = etl"

    def test_toDataPipeline2Config_multi(self):
        output = self._run('print({"pipeline": "etl", "schedule": "hourly"}.toDataPipeline2Config())')
        assert output[-1] == "pipeline = etl\nschedule = hourly"
