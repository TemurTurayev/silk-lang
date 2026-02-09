"""
Tests for dict .toSecurityHub3Config() method - format dict as SecurityHub3 config.
"""

from silk.interpreter import Interpreter


class TestDictToSecurityHub3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSecurityHub3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toSecurityHub3Config())')
        assert output[-1] == "host = localhost"

    def test_toSecurityHub3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toSecurityHub3Config())')
        assert output[-1] == "host = localhost\nport = 443"
