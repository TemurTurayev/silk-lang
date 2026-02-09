"""
Tests for dict .toNeptune2Config() method - format as Neptune config.
"""

from silk.interpreter import Interpreter


class TestDictToNeptune2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNeptune2Config_basic(self):
        output = self._run('print({"clusterName": "graph-db"}.toNeptune2Config())')
        assert output[-1] == "clusterName = graph-db"

    def test_toNeptune2Config_multi(self):
        output = self._run('print({"clusterName": "graph-db", "engine": "neptune"}.toNeptune2Config())')
        assert "clusterName = graph-db" in output[-1]
