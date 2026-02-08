"""
Tests for dict .toBeamConfig() method - format as Beam config.
"""

from silk.interpreter import Interpreter


class TestDictToBeamConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBeamConfig_basic(self):
        output = self._run('print({"runner": "local"}.toBeamConfig())')
        assert output[-1] == "runner = local"

    def test_toBeamConfig_multi(self):
        output = self._run('print({"workers": 4, "streaming": true}.toBeamConfig())')
        assert "streaming = true" in output[-1]
