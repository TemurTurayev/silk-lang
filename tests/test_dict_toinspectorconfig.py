"""
Tests for dict .toInspectorConfig() method - format as Inspector config.
"""

from silk.interpreter import Interpreter


class TestDictToInspectorConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toInspectorConfig_basic(self):
        output = self._run('print({"target": "ec2"}.toInspectorConfig())')
        assert output[-1] == "target = ec2"

    def test_toInspectorConfig_multi(self):
        output = self._run('print({"schedule": "weekly", "severity": "high"}.toInspectorConfig())')
        assert "schedule = weekly" in output[-1]
