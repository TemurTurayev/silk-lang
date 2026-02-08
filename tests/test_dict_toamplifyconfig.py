"""
Tests for dict .toAmplifyConfig() method - format as Amplify config.
"""

from silk.interpreter import Interpreter


class TestDictToAmplifyConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAmplifyConfig_basic(self):
        output = self._run('print({"framework": "react"}.toAmplifyConfig())')
        assert output[-1] == "framework = react"

    def test_toAmplifyConfig_multi(self):
        output = self._run('print({"hosting": "s3", "ssl": true}.toAmplifyConfig())')
        assert "hosting = s3" in output[-1]
