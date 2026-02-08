"""
Tests for dict .toStepFunctions2Config() method - format as Step Functions config.
"""

from silk.interpreter import Interpreter


class TestDictToStepFunctions2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toStepFunctions2Config_basic(self):
        output = self._run('print({"stateMachine": "my-workflow"}.toStepFunctions2Config())')
        assert output[-1] == "stateMachine = my-workflow"

    def test_toStepFunctions2Config_multi(self):
        output = self._run('print({"stateMachine": "my-workflow", "timeout": 300}.toStepFunctions2Config())')
        assert "stateMachine = my-workflow" in output[-1]
