"""
Tests for dict .toPersonalize2Config() method - format as Personalize v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToPersonalize2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPersonalize2Config_basic(self):
        output = self._run('print({"dataset": "myDataset"}.toPersonalize2Config())')
        assert output[-1] == "dataset = myDataset"

    def test_toPersonalize2Config_multi(self):
        output = self._run('print({"dataset": "users", "campaign": "recs"}.toPersonalize2Config())')
        assert output[-1] == "dataset = users\ncampaign = recs"
