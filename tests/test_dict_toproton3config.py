"""
Tests for dict .toProton3Config() method - format dict as Proton3 config.
"""

from silk.interpreter import Interpreter


class TestDictToProton3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toProton3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toProton3Config())')
        assert output[-1] == "host = localhost"

    def test_toProton3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toProton3Config())')
        assert output[-1] == "host = localhost\nport = 443"
