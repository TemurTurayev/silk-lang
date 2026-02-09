"""
Tests for dict .toBatch3Config() method - format dict as Batch3 config.
"""

from silk.interpreter import Interpreter


class TestDictToBatch3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBatch3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toBatch3Config())')
        assert output[-1] == "host = localhost"

    def test_toBatch3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toBatch3Config())')
        assert output[-1] == "host = localhost\nport = 443"
