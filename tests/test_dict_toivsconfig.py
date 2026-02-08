"""
Tests for dict .toIVSConfig() method - format as Amazon IVS config.
"""

from silk.interpreter import Interpreter


class TestDictToIVSConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIVSConfig_basic(self):
        output = self._run('print({"channel": "stream1"}.toIVSConfig())')
        assert output[-1] == "channel = stream1"

    def test_toIVSConfig_multi(self):
        output = self._run('print({"channel": "stream1", "type": "basic"}.toIVSConfig())')
        assert "channel = stream1" in output[-1]
