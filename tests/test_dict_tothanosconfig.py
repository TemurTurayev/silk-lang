"""
Tests for dict .toThanosConfig() method - format as Thanos config.
"""

from silk.interpreter import Interpreter


class TestDictToThanosConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toThanosConfig_basic(self):
        output = self._run('print({"store": "s3"}.toThanosConfig())')
        assert output[-1] == "store = s3"

    def test_toThanosConfig_multi(self):
        output = self._run('print({"port": 10901, "active": true}.toThanosConfig())')
        assert "active = true" in output[-1]
