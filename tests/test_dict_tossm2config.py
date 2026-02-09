"""
Tests for dict .toSSM2Config() method - format as SSM v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToSSM2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSSM2Config_basic(self):
        output = self._run('print({"document": "runbook"}.toSSM2Config())')
        assert output[-1] == "document = runbook"

    def test_toSSM2Config_multi(self):
        output = self._run('print({"document": "runbook", "target": "ec2"}.toSSM2Config())')
        assert output[-1] == "document = runbook\ntarget = ec2"
