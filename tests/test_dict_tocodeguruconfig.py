"""
Tests for dict .toCodeGuruConfig() method - format as CodeGuru config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeGuruConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeGuruConfig_basic(self):
        output = self._run('print({"profiler": "enabled"}.toCodeGuruConfig())')
        assert output[-1] == "profiler = enabled"

    def test_toCodeGuruConfig_multi(self):
        output = self._run('print({"reviewer": true, "threshold": 80}.toCodeGuruConfig())')
        assert "threshold = 80" in output[-1]
