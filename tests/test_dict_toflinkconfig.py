"""
Tests for dict .toFlinkConfig() method - format as Flink config.
"""

from silk.interpreter import Interpreter


class TestDictToFlinkConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFlinkConfig_basic(self):
        output = self._run('print({"parallelism": 4}.toFlinkConfig())')
        assert output[-1] == "parallelism = 4"

    def test_toFlinkConfig_multi(self):
        output = self._run('print({"mode": "batch", "slots": 8}.toFlinkConfig())')
        assert "slots = 8" in output[-1]
