"""
Tests for dict .toEMRConfig() method - format as EMR config.
"""

from silk.interpreter import Interpreter


class TestDictToEMRConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEMRConfig_basic(self):
        output = self._run('print({"cluster": "spark"}.toEMRConfig())')
        assert output[-1] == "cluster = spark"

    def test_toEMRConfig_multi(self):
        output = self._run('print({"instances": 5, "type": "m5"}.toEMRConfig())')
        assert "instances = 5" in output[-1]
