"""
Tests for dict .toGlueConfig() method - format as Glue config.
"""

from silk.interpreter import Interpreter


class TestDictToGlueConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGlueConfig_basic(self):
        output = self._run('print({"crawler": "daily"}.toGlueConfig())')
        assert output[-1] == "crawler = daily"

    def test_toGlueConfig_multi(self):
        output = self._run('print({"workers": 10, "timeout": 300}.toGlueConfig())')
        assert "workers = 10" in output[-1]
