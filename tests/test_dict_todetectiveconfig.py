"""
Tests for dict .toDetectiveConfig() method - format as Detective config.
"""

from silk.interpreter import Interpreter


class TestDictToDetectiveConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDetectiveConfig_basic(self):
        output = self._run('print({"graph": "main"}.toDetectiveConfig())')
        assert output[-1] == "graph = main"

    def test_toDetectiveConfig_multi(self):
        output = self._run('print({"region": "us-east-1", "scope": "org"}.toDetectiveConfig())')
        assert "region = us-east-1" in output[-1]
