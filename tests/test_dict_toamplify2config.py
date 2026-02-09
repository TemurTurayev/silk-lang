"""
Tests for dict .toAmplify2Config() method - format as Amplify config.
"""

from silk.interpreter import Interpreter


class TestDictToAmplify2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAmplify2Config_basic(self):
        output = self._run('print({"appName": "my-app"}.toAmplify2Config())')
        assert output[-1] == "appName = my-app"

    def test_toAmplify2Config_multi(self):
        output = self._run('print({"appName": "my-app", "framework": "react"}.toAmplify2Config())')
        assert "appName = my-app" in output[-1]
