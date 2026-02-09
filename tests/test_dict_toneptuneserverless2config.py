"""
Tests for dict .toNeptuneServerless2Config() method - format as Neptune Serverless config.
"""

from silk.interpreter import Interpreter


class TestDictToNeptuneServerless2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNeptuneServerless2Config_basic(self):
        output = self._run('print({"dbCluster": "serverless-graph"}.toNeptuneServerless2Config())')
        assert output[-1] == "dbCluster = serverless-graph"

    def test_toNeptuneServerless2Config_multi(self):
        output = self._run('print({"dbCluster": "serverless-graph", "maxCapacity": 128}.toNeptuneServerless2Config())')
        assert "dbCluster = serverless-graph" in output[-1]
