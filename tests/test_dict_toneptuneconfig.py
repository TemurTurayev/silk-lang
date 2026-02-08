"""
Tests for dict .toNeptuneConfig() method - format as Neptune config.
"""

from silk.interpreter import Interpreter


class TestDictToNeptuneConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNeptuneConfig_basic(self):
        output = self._run('print({"engine": "gremlin"}.toNeptuneConfig())')
        assert output[-1] == "engine = gremlin"

    def test_toNeptuneConfig_multi(self):
        output = self._run('print({"instance": "db.r5.large", "replicas": 2}.toNeptuneConfig())')
        assert "replicas = 2" in output[-1]
