"""
Tests for dict .toWorkSpaces3Config() method - format dict as WorkSpaces3 config.
"""

from silk.interpreter import Interpreter


class TestDictToWorkSpaces3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toWorkSpaces3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toWorkSpaces3Config())')
        assert output[-1] == "host = localhost"

    def test_toWorkSpaces3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toWorkSpaces3Config())')
        assert output[-1] == "host = localhost\nport = 443"
