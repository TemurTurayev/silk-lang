"""
Tests for dict .toAppRunner2Config() method - format as AppRunner config.
"""

from silk.interpreter import Interpreter


class TestDictToAppRunner2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppRunner2Config_basic(self):
        output = self._run('print({"serviceName": "my-svc"}.toAppRunner2Config())')
        assert output[-1] == "serviceName = my-svc"

    def test_toAppRunner2Config_multi(self):
        output = self._run('print({"serviceName": "my-svc", "port": 8080}.toAppRunner2Config())')
        assert "serviceName = my-svc" in output[-1]
