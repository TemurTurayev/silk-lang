"""
Tests for dict .toRoute532Config() method - format as Route53 v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToRoute532Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRoute532Config_basic(self):
        output = self._run('print({"zone": "example.com"}.toRoute532Config())')
        assert output[-1] == "zone = example.com"

    def test_toRoute532Config_multi(self):
        output = self._run('print({"zone": "example.com", "type": "A"}.toRoute532Config())')
        assert output[-1] == "zone = example.com\ntype = A"
