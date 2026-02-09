"""
Tests for dict .toPersonalize3Config() method - format as Personalize v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToPersonalize3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPersonalize3Config_basic(self):
        output = self._run('print({"campaign": "summer-sale"}.toPersonalize3Config())')
        assert output[-1] == "campaign = summer-sale"

    def test_toPersonalize3Config_multi(self):
        output = self._run('print({"campaign": "summer-sale", "region": "us-east-1"}.toPersonalize3Config())')
        assert output[-1] == "campaign = summer-sale\nregion = us-east-1"
