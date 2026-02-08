"""
Tests for dict .toOrganizationsConfig() method - format as Organizations config.
"""

from silk.interpreter import Interpreter


class TestDictToOrganizationsConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOrganizationsConfig_basic(self):
        output = self._run('print({"root": "r-abc123"}.toOrganizationsConfig())')
        assert output[-1] == "root = r-abc123"

    def test_toOrganizationsConfig_multi(self):
        output = self._run('print({"feature": "all", "policy": "scp"}.toOrganizationsConfig())')
        assert "feature = all" in output[-1]
