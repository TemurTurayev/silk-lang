"""
Tests for dict .toOpsWorks3Config() method - format dict as OpsWorks3 config.
"""

from silk.interpreter import Interpreter


class TestDictToOpsWorks3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOpsWorks3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toOpsWorks3Config())')
        assert output[-1] == "host = localhost"

    def test_toOpsWorks3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toOpsWorks3Config())')
        assert output[-1] == "host = localhost\nport = 443"
