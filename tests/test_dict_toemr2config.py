"""
Tests for dict .toEMR2Config() method - format as EMR config.
"""

from silk.interpreter import Interpreter


class TestDictToEMR2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEMR2Config_basic(self):
        output = self._run('print({"clusterName": "my-cluster"}.toEMR2Config())')
        assert output[-1] == "clusterName = my-cluster"

    def test_toEMR2Config_multi(self):
        output = self._run('print({"clusterName": "my-cluster", "releaseLabel": "emr-6.0"}.toEMR2Config())')
        assert "clusterName = my-cluster" in output[-1]
