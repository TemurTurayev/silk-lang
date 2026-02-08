"""
Tests for dict .toMWAAConfig() method - format as MWAA (Managed Workflows for Apache Airflow) config.
"""

from silk.interpreter import Interpreter


class TestDictToMWAAConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMWAAConfig_basic(self):
        output = self._run('print({"env": "production"}.toMWAAConfig())')
        assert output[-1] == "env = production"

    def test_toMWAAConfig_multi(self):
        output = self._run('print({"workers": 4, "scheduler": "celery"}.toMWAAConfig())')
        assert "workers = 4" in output[-1]
