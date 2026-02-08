"""
Tests for dict .toPulsarConfig() method - format as Pulsar config.
"""

from silk.interpreter import Interpreter


class TestDictToPulsarConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPulsarConfig_basic(self):
        output = self._run('print({"tenant": "public"}.toPulsarConfig())')
        assert output[-1] == "tenant = public"

    def test_toPulsarConfig_multi(self):
        output = self._run('print({"partitions": 3, "persistent": true}.toPulsarConfig())')
        assert "persistent = true" in output[-1]
