"""
Tests for dict .toAppStream3Config() method - format dict as AppStream3 config.
"""

from silk.interpreter import Interpreter


class TestDictToAppStream3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppStream3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toAppStream3Config())')
        assert output[-1] == "host = localhost"

    def test_toAppStream3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toAppStream3Config())')
        assert output[-1] == "host = localhost\nport = 443"
