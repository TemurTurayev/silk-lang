"""
Tests for dict .toConnect2Config() method - format as Connect v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToConnect2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toConnect2Config_basic(self):
        output = self._run('print({"instance": "prod"}.toConnect2Config())')
        assert output[-1] == "instance = prod"

    def test_toConnect2Config_multi(self):
        output = self._run('print({"instance": "prod", "queue": "basic"}.toConnect2Config())')
        assert output[-1] == "instance = prod\nqueue = basic"
