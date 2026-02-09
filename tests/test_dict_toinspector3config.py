"""
Tests for dict .toInspector3Config() method - format dict as Inspector3 config.
"""

from silk.interpreter import Interpreter


class TestDictToInspector3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toInspector3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toInspector3Config())')
        assert output[-1] == "host = localhost"

    def test_toInspector3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toInspector3Config())')
        assert output[-1] == "host = localhost\nport = 443"
