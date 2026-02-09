"""
Tests for dict .toMediaLive3Config() method - format dict as MediaLive3 config.
"""

from silk.interpreter import Interpreter


class TestDictToMediaLive3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaLive3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toMediaLive3Config())')
        assert output[-1] == "host = localhost"

    def test_toMediaLive3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toMediaLive3Config())')
        assert output[-1] == "host = localhost\nport = 443"
