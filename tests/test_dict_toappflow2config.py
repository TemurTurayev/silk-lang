"""
Tests for dict .toAppFlow2Config() method - format as AppFlow config.
"""

from silk.interpreter import Interpreter


class TestDictToAppFlow2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppFlow2Config_basic(self):
        output = self._run('print({"flowName": "my-flow"}.toAppFlow2Config())')
        assert output[-1] == "flowName = my-flow"

    def test_toAppFlow2Config_multi(self):
        output = self._run('print({"flowName": "my-flow", "source": "salesforce"}.toAppFlow2Config())')
        assert "flowName = my-flow" in output[-1]
