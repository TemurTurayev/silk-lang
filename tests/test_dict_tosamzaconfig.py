"""
Tests for dict .toSamzaConfig() method - format as Samza config.
"""

from silk.interpreter import Interpreter


class TestDictToSamzaConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSamzaConfig_basic(self):
        output = self._run('print({"job": "processor"}.toSamzaConfig())')
        assert output[-1] == "job = processor"

    def test_toSamzaConfig_multi(self):
        output = self._run('print({"threads": 2, "async": true}.toSamzaConfig())')
        assert "async = true" in output[-1]
