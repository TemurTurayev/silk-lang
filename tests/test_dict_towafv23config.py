"""
Tests for dict .toWAFv23Config() method - format dict as WAFv23 config.
"""

from silk.interpreter import Interpreter


class TestDictToWAFv23Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toWAFv23Config_basic(self):
        output = self._run('print({"host": "localhost"}.toWAFv23Config())')
        assert output[-1] == "host = localhost"

    def test_toWAFv23Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toWAFv23Config())')
        assert output[-1] == "host = localhost\nport = 443"
