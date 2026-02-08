"""
Tests for dict .toAppSyncConfig() method - format as AppSync config.
"""

from silk.interpreter import Interpreter


class TestDictToAppSyncConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppSyncConfig_basic(self):
        output = self._run('print({"api": "graphql"}.toAppSyncConfig())')
        assert output[-1] == "api = graphql"

    def test_toAppSyncConfig_multi(self):
        output = self._run('print({"auth": "cognito", "cache": true}.toAppSyncConfig())')
        assert "auth = cognito" in output[-1]
