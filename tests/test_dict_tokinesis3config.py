"""
Tests for dict .toKinesis3Config() method - alias for toGrafanaConfig.
"""

from silk.interpreter import Interpreter


class TestDictToKinesis3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKinesis3Config_basic(self):
        output = self._run('print({"host": "localhost", "port": 3000}.toKinesis3Config())')
        assert 'host = localhost' in output[-1]
        assert 'port = 3000' in output[-1]

    def test_toKinesis3Config_multi(self):
        output = self._run('print({"a": 1, "b": 2, "c": 3}.toKinesis3Config())')
        assert 'a = 1' in output[-1]
        assert 'c = 3' in output[-1]
