"""
Tests for dict .toStormConfig() method - format as Storm config.
"""

from silk.interpreter import Interpreter


class TestDictToStormConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toStormConfig_basic(self):
        output = self._run('print({"topology": "main"}.toStormConfig())')
        assert output[-1] == "topology = main"

    def test_toStormConfig_multi(self):
        output = self._run('print({"workers": 4, "debug": false}.toStormConfig())')
        assert "debug = false" in output[-1]
