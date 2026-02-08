"""
Tests for dict .toDataSyncConfig() method - format as AWS DataSync config.
"""

from silk.interpreter import Interpreter


class TestDictToDataSyncConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDataSyncConfig_basic(self):
        output = self._run('print({"source": "s3"}.toDataSyncConfig())')
        assert output[-1] == "source = s3"

    def test_toDataSyncConfig_multi(self):
        output = self._run('print({"source": "s3", "dest": "efs"}.toDataSyncConfig())')
        assert "source = s3" in output[-1]
