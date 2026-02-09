"""
Tests for dict .toCognito3Config() method - format as Cognito v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCognito3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCognito3Config_basic(self):
        output = self._run('print({"pool": "us-pool"}.toCognito3Config())')
        assert output[-1] == "pool = us-pool"

    def test_toCognito3Config_multi(self):
        output = self._run('print({"pool": "us-pool", "client": "web"}.toCognito3Config())')
        assert output[-1] == "pool = us-pool\nclient = web"
