"""
Tests for dict .toDocDB2Config() method - format as DocumentDB config.
"""

from silk.interpreter import Interpreter


class TestDictToDocDB2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDocDB2Config_basic(self):
        output = self._run('print({"clusterName": "doc-cluster"}.toDocDB2Config())')
        assert output[-1] == "clusterName = doc-cluster"

    def test_toDocDB2Config_multi(self):
        output = self._run('print({"clusterName": "doc-cluster", "engine": "docdb"}.toDocDB2Config())')
        assert "clusterName = doc-cluster" in output[-1]
