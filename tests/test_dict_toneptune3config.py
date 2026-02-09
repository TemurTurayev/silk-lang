"""
Tests for dict .toNeptune3Config() method - format as Neptune v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToNeptune3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNeptune3Config_basic(self):
        output = self._run('print({"engine": "neptune"}.toNeptune3Config())')
        assert output[-1] == "engine = neptune"

    def test_toNeptune3Config_multi(self):
        output = self._run('print({"engine": "neptune", "instances": 3}.toNeptune3Config())')
        assert output[-1] == "engine = neptune\ninstances = 3"
