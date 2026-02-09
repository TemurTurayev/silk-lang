"""
Tests for dict .toCognito2Config() method - format as Cognito config.
"""

from silk.interpreter import Interpreter


class TestDictToCognito2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCognito2Config_basic(self):
        output = self._run('print({"poolName": "my-pool"}.toCognito2Config())')
        assert output[-1] == "poolName = my-pool"

    def test_toCognito2Config_multi(self):
        output = self._run('print({"poolName": "my-pool", "region": "us-east-1"}.toCognito2Config())')
        assert "poolName = my-pool" in output[-1]
