"""
Tests for dict .toCodeStar3Config() method - format as CodeStar v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCodeStar3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeStar3Config_basic(self):
        output = self._run('print({"project": "my-project"}.toCodeStar3Config())')
        assert output[-1] == "project = my-project"

    def test_toCodeStar3Config_multi(self):
        output = self._run('print({"project": "my-project", "template": "webapp"}.toCodeStar3Config())')
        assert output[-1] == "project = my-project\ntemplate = webapp"
