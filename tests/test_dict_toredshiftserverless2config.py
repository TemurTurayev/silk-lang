"""
Tests for dict .toRedshiftServerless2Config() method - format as Redshift Serverless config.
"""

from silk.interpreter import Interpreter


class TestDictToRedshiftServerless2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRedshiftServerless2Config_basic(self):
        output = self._run('print({"namespaceName": "analytics"}.toRedshiftServerless2Config())')
        assert output[-1] == "namespaceName = analytics"

    def test_toRedshiftServerless2Config_multi(self):
        output = self._run('print({"namespaceName": "analytics", "baseCapacity": 32}.toRedshiftServerless2Config())')
        assert "namespaceName = analytics" in output[-1]
