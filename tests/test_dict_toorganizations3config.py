"""
Tests for dict .toOrganizations3Config() method - format dict as Organizations3 config.
"""

from silk.interpreter import Interpreter


class TestDictToOrganizations3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOrganizations3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toOrganizations3Config())')
        assert output[-1] == "host = localhost"

    def test_toOrganizations3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toOrganizations3Config())')
        assert output[-1] == "host = localhost\nport = 443"
