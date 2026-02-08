"""
Tests for dict .toPyroscopeConfig() method - format as Pyroscope config.
"""

from silk.interpreter import Interpreter


class TestDictToPyroscopeConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPyroscopeConfig_basic(self):
        output = self._run('print({"app": "myservice"}.toPyroscopeConfig())')
        assert output[-1] == "app = myservice"

    def test_toPyroscopeConfig_multi(self):
        output = self._run('print({"port": 4040, "enabled": true}.toPyroscopeConfig())')
        assert "enabled = true" in output[-1]
