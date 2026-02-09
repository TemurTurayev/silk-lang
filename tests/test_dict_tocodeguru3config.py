"""
Tests for dict .toCodeGuru3Config() method - format as CodeGuru v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCodeGuru3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeGuru3Config_basic(self):
        output = self._run('print({"profiler": "my-app"}.toCodeGuru3Config())')
        assert output[-1] == "profiler = my-app"

    def test_toCodeGuru3Config_multi(self):
        output = self._run('print({"profiler": "my-app", "reviewer": "enabled"}.toCodeGuru3Config())')
        assert output[-1] == "profiler = my-app\nreviewer = enabled"
