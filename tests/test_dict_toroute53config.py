"""
Tests for dict .toRoute53Config() method - format as Route53 config.
"""

from silk.interpreter import Interpreter


class TestDictToRoute53Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRoute53Config_basic(self):
        output = self._run('print({"zone": "example.com"}.toRoute53Config())')
        assert output[-1] == "zone = example.com"

    def test_toRoute53Config_multi(self):
        output = self._run('print({"ttl": 300, "type": "A"}.toRoute53Config())')
        assert "type = A" in output[-1]
