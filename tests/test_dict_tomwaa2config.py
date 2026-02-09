"""
Tests for dict .toMWAA2Config() method - format as MWAA config.
"""

from silk.interpreter import Interpreter


class TestDictToMWAA2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMWAA2Config_basic(self):
        output = self._run('print({"envName": "airflow-env"}.toMWAA2Config())')
        assert output[-1] == "envName = airflow-env"

    def test_toMWAA2Config_multi(self):
        output = self._run('print({"envName": "airflow-env", "dagS3Path": "dags/"}.toMWAA2Config())')
        assert "envName = airflow-env" in output[-1]
