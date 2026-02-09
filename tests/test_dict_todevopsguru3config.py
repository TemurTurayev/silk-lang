"""
Tests for dict .toDevOpsGuru3Config() method - format dict as DevOpsGuru3 config.
"""

from silk.interpreter import Interpreter


class TestDictToDevOpsGuru3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDevOpsGuru3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toDevOpsGuru3Config())')
        assert output[-1] == "host = localhost"

    def test_toDevOpsGuru3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toDevOpsGuru3Config())')
        assert output[-1] == "host = localhost\nport = 443"
