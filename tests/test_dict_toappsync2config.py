"""
Tests for dict .toAppSync2Config() method - format as AppSync config.
"""

from silk.interpreter import Interpreter


class TestDictToAppSync2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppSync2Config_basic(self):
        output = self._run('print({"apiName": "my-api"}.toAppSync2Config())')
        assert output[-1] == "apiName = my-api"

    def test_toAppSync2Config_multi(self):
        output = self._run('print({"apiName": "my-api", "authType": "API_KEY"}.toAppSync2Config())')
        assert "apiName = my-api" in output[-1]
