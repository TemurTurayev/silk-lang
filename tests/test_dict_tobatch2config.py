"""
Tests for dict .toBatch2Config() method - format as Batch v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToBatch2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBatch2Config_basic(self):
        output = self._run('print({"queue": "default"}.toBatch2Config())')
        assert output[-1] == "queue = default"

    def test_toBatch2Config_multi(self):
        output = self._run('print({"queue": "default", "priority": "10"}.toBatch2Config())')
        assert output[-1] == "queue = default\npriority = 10"
