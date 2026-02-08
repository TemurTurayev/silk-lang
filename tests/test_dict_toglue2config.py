"""
Tests for dict .toGlue2Config() method - format as Glue config.
"""

from silk.interpreter import Interpreter


class TestDictToGlue2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGlue2Config_basic(self):
        output = self._run('print({"jobName": "etl-job"}.toGlue2Config())')
        assert output[-1] == "jobName = etl-job"

    def test_toGlue2Config_multi(self):
        output = self._run('print({"jobName": "etl-job", "workerType": "G.1X"}.toGlue2Config())')
        assert "jobName = etl-job" in output[-1]
