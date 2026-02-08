"""
Tests for dict .toCognitoConfig() method - format as Cognito config.
"""

from silk.interpreter import Interpreter


class TestDictToCognitoConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCognitoConfig_basic(self):
        output = self._run('print({"pool": "users"}.toCognitoConfig())')
        assert output[-1] == "pool = users"

    def test_toCognitoConfig_multi(self):
        output = self._run('print({"mfa": true, "password_min": 8}.toCognitoConfig())')
        assert "password_min = 8" in output[-1]
