"""
Tests for dict .toWAFv2Config() method - format as WAFv2 config.
"""

from silk.interpreter import Interpreter


class TestDictToWAFv2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toWAFv2Config_basic(self):
        output = self._run('print({"scope": "regional"}.toWAFv2Config())')
        assert output[-1] == "scope = regional"

    def test_toWAFv2Config_multi(self):
        output = self._run('print({"rule": "rateLimit", "limit": 2000}.toWAFv2Config())')
        assert "rule = rateLimit" in output[-1]
