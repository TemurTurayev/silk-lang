"""
Tests for dict .toAccessAnalyzer3Config() method - format dict as AccessAnalyzer3 config.
"""

from silk.interpreter import Interpreter


class TestDictToAccessAnalyzer3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAccessAnalyzer3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toAccessAnalyzer3Config())')
        assert output[-1] == "host = localhost"

    def test_toAccessAnalyzer3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toAccessAnalyzer3Config())')
        assert output[-1] == "host = localhost\nport = 443"
