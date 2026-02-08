"""
Tests for dict .toStepFunctionsConfig() method - format as Step Functions config.
"""

from silk.interpreter import Interpreter


class TestDictToStepFunctionsConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toStepFunctionsConfig_basic(self):
        output = self._run('print({"state": "running"}.toStepFunctionsConfig())')
        assert output[-1] == "state = running"

    def test_toStepFunctionsConfig_multi(self):
        output = self._run('print({"retries": 3, "timeout": 60}.toStepFunctionsConfig())')
        assert "timeout = 60" in output[-1]
