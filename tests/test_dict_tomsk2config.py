"""
Tests for dict .toMSK2Config() method - format as MSK v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToMSK2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMSK2Config_basic(self):
        output = self._run('print({"cluster": "main"}.toMSK2Config())')
        assert output[-1] == "cluster = main"

    def test_toMSK2Config_multi(self):
        output = self._run('print({"cluster": "main", "brokers": "3"}.toMSK2Config())')
        assert output[-1] == "cluster = main\nbrokers = 3"
