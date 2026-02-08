"""
Tests for dict .toBatchConfig() method - format as AWS Batch config.
"""

from silk.interpreter import Interpreter


class TestDictToBatchConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBatchConfig_basic(self):
        output = self._run('print({"queue": "default"}.toBatchConfig())')
        assert output[-1] == "queue = default"

    def test_toBatchConfig_multi(self):
        output = self._run('print({"type": "managed", "vcpus": "4"}.toBatchConfig())')
        assert "type = managed" in output[-1]
