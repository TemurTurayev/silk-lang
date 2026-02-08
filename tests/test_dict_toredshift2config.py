"""
Tests for dict .toRedshift2Config() method - format as Redshift config.
"""

from silk.interpreter import Interpreter


class TestDictToRedshift2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRedshift2Config_basic(self):
        output = self._run('print({"clusterIdentifier": "my-cluster"}.toRedshift2Config())')
        assert output[-1] == "clusterIdentifier = my-cluster"

    def test_toRedshift2Config_multi(self):
        output = self._run('print({"clusterIdentifier": "my-cluster", "nodeType": "dc2.large"}.toRedshift2Config())')
        assert "clusterIdentifier = my-cluster" in output[-1]
