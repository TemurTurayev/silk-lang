"""
Tests for dict .toNeptuneServerlessConfig() method - format as Neptune Serverless config.
"""

from silk.interpreter import Interpreter


class TestDictToNeptuneServerlessConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNeptuneServerlessConfig_basic(self):
        output = self._run('print({"engine": "sparql"}.toNeptuneServerlessConfig())')
        assert output[-1] == "engine = sparql"

    def test_toNeptuneServerlessConfig_multi(self):
        output = self._run('print({"min_ncu": 1, "max_ncu": 128}.toNeptuneServerlessConfig())')
        assert "min_ncu = 1" in output[-1]
