"""
Tests for dict .toAppFlowConfig() method - format as AppFlow config.
"""

from silk.interpreter import Interpreter


class TestDictToAppFlowConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppFlowConfig_basic(self):
        output = self._run('print({"source": "salesforce"}.toAppFlowConfig())')
        assert output[-1] == "source = salesforce"

    def test_toAppFlowConfig_multi(self):
        output = self._run('print({"trigger": "event", "dest": "s3"}.toAppFlowConfig())')
        assert "dest = s3" in output[-1]
