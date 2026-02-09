"""
Tests for dict .toCUR3Config() method - format dict as CUR3 config.
"""

from silk.interpreter import Interpreter


class TestDictToCUR3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCUR3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toCUR3Config())')
        assert output[-1] == "host = localhost"

    def test_toCUR3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toCUR3Config())')
        assert output[-1] == "host = localhost\nport = 443"
