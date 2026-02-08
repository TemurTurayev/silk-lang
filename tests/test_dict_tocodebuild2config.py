"""
Tests for dict .toCodeBuild2Config() method - format as CodeBuild config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeBuild2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeBuild2Config_basic(self):
        output = self._run('print({"projectName": "my-build"}.toCodeBuild2Config())')
        assert output[-1] == "projectName = my-build"

    def test_toCodeBuild2Config_multi(self):
        output = self._run('print({"projectName": "my-build", "computeType": "BUILD_GENERAL1_SMALL"}.toCodeBuild2Config())')
        assert "projectName = my-build" in output[-1]
