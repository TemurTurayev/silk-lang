"""
Tests for dict .toWorkSpaces2Config() method - format as WorkSpaces v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToWorkSpaces2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toWorkSpaces2Config_basic(self):
        output = self._run('print({"bundle": "standard"}.toWorkSpaces2Config())')
        assert output[-1] == "bundle = standard"

    def test_toWorkSpaces2Config_multi(self):
        output = self._run('print({"bundle": "standard", "mode": "auto"}.toWorkSpaces2Config())')
        assert output[-1] == "bundle = standard\nmode = auto"
