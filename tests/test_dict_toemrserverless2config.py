"""
Tests for dict .toEMRServerless2Config() method - format as EMR Serverless config.
"""

from silk.interpreter import Interpreter


class TestDictToEMRServerless2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEMRServerless2Config_basic(self):
        output = self._run('print({"appName": "spark-app"}.toEMRServerless2Config())')
        assert output[-1] == "appName = spark-app"

    def test_toEMRServerless2Config_multi(self):
        output = self._run('print({"appName": "spark-app", "releaseLabel": "emr-6.9.0"}.toEMRServerless2Config())')
        assert "appName = spark-app" in output[-1]
