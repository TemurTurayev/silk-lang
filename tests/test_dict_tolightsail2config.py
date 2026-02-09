"""
Tests for dict .toLightsail2Config() method - format as Lightsail v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToLightsail2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLightsail2Config_basic(self):
        output = self._run('print({"plan": "micro"}.toLightsail2Config())')
        assert output[-1] == "plan = micro"

    def test_toLightsail2Config_multi(self):
        output = self._run('print({"plan": "micro", "os": "linux"}.toLightsail2Config())')
        assert output[-1] == "plan = micro\nos = linux"
