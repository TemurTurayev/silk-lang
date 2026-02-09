"""
Tests for dict .toMediaStore2Config() method - format as MediaStore v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToMediaStore2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaStore2Config_basic(self):
        output = self._run('print({"container": "assets"}.toMediaStore2Config())')
        assert output[-1] == "container = assets"

    def test_toMediaStore2Config_multi(self):
        output = self._run('print({"container": "assets", "policy": "read"}.toMediaStore2Config())')
        assert output[-1] == "container = assets\npolicy = read"
