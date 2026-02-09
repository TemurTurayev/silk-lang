"""
Tests for dict .toAmplify3Config() method - format as Amplify v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToAmplify3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAmplify3Config_basic(self):
        output = self._run('print({"app": "myapp"}.toAmplify3Config())')
        assert output[-1] == "app = myapp"

    def test_toAmplify3Config_multi(self):
        output = self._run('print({"app": "myapp", "env": "prod"}.toAmplify3Config())')
        assert output[-1] == "app = myapp\nenv = prod"
