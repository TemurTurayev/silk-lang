"""
Tests for dict .toDetective3Config() method - format dict as Detective3 config.
"""

from silk.interpreter import Interpreter


class TestDictToDetective3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDetective3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toDetective3Config())')
        assert output[-1] == "host = localhost"

    def test_toDetective3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toDetective3Config())')
        assert output[-1] == "host = localhost\nport = 443"
