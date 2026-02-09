"""
Tests for dict .toCodeStar2Config() method - format as CodeStar config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeStar2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeStar2Config_basic(self):
        output = self._run('print({"projectName": "my-project"}.toCodeStar2Config())')
        assert output[-1] == "projectName = my-project"

    def test_toCodeStar2Config_multi(self):
        output = self._run('print({"projectName": "my-project", "region": "us-east-1"}.toCodeStar2Config())')
        assert "projectName = my-project" in output[-1]
