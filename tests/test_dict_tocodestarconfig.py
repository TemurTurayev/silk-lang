"""
Tests for dict .toCodeStarConfig() method - format as CodeStar config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeStarConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeStarConfig_basic(self):
        output = self._run('print({"project": "webapp"}.toCodeStarConfig())')
        assert output[-1] == "project = webapp"

    def test_toCodeStarConfig_multi(self):
        output = self._run('print({"template": "express", "region": "us-west-2"}.toCodeStarConfig())')
        assert "template = express" in output[-1]
