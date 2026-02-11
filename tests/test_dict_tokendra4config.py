"""
Tests for dict .toKendra4Config() method - alias for toGrafanaConfig.
"""

from silk.interpreter import Interpreter


class TestDictToKendra4Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKendra4Config_basic(self):
        output = self._run('print({"host": "localhost", "port": 3000}.toKendra4Config())')
        assert 'host = localhost' in output[-1]
        assert 'port = 3000' in output[-1]

    def test_toKendra4Config_multi(self):
        output = self._run('print({"a": 1, "b": 2, "c": 3}.toKendra4Config())')
        assert 'a = 1' in output[-1]
        assert 'c = 3' in output[-1]
